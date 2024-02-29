from random import random
from pathlib import Path
from string import ascii_lowercase

import click
from pydub import AudioSegment
from pydub.playback import play as play_sound


root_sounds = Path('animalese_generator\\resources\\sounds')
sound_key_bank = list(ascii_lowercase)
sound_key_bank.extend(['th','sh',' ','.'])


@click.command()
@click.option(
    '-m',
    '--message',
    type=click.STRING,
    help='words of the sentence'
)
@click.option(
    '-p',
    '--pitch',
    type=click.Choice(['high', 'med', 'low', 'lowest']),
    default="med",
    help="voice pitch, choose between 'high', 'med', 'low' or 'lowest'"
)
@click.option(
    '-o',
    '--out',
    type=click.Path(file_okay=True, dir_okay=False, path_type=Path),
    default=None,
    help="output file"
)
@click.option(
    '--play',
    is_flag=True,
    show_default=True,
    default=False,
    help="playback sound"
)
def generate_audio(message: str, pitch, out, play):
    randomize_factor = .35 if pitch == 'med' else .25

    sounds = {}

    for index, key in enumerate(sound_key_bank, 1):
        sounds[key] = AudioSegment.from_wav(root_sounds / pitch / f'sound{index:0>2}.wav')

    sound = None

    gen_octave = lambda predicate: random() * randomize_factor + (index-index*.8) * .1 + 2.1 if predicate else random() * randomize_factor + 2.0

    for i, char in enumerate(message.lower()):
        if not char.isalpha() or char == '.':
            continue
        if char in ('s', 't') and i < len(message) - 1 and message[i + 1] == 'h':
            current = sounds[f'{char}h']
        elif char == 'h' and message[i - 1] in ('s', 't'):
            continue # Sanity check if we had our composite sound of sh or th
        elif char in (',', '?'):
            current = sounds['.']
        else:
            current = sounds[char]
        
        if message.endswith('?'):
            octaves = gen_octave(i >= len(message) * 0.8)
        else:
            octaves = random() * randomize_factor + 2.3
        new_sample_rate = int(current.frame_rate * (2.0 ** octaves))
        new_sound = current._spawn(current.raw_data, overrides={'frame_rate': new_sample_rate})
        sound = new_sound if not sound else sound + new_sound.set_frame_rate(44100) # ^ the fuck? What's the point?
    
    if out:
        sound.export(out, format='wav')
    
    if play:
        play_sound(sound)


if __name__ == '__main__':
    generate_audio()
