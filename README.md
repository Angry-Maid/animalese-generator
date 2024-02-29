# Animalese Audio Generator

## General info
This project allows you to generate audio from text in the style of animalese from the Animal Crossing games. 

## Usage

```sh
$ py animalese_generator/main.py -m "the quick brown fox jumps over the lazy dog" --out output.wav
```
or to play sound
```sh
$ py animalese_generator/main.py -m "the quick brown fox jumps over the lazy dog" --play
```

The program accepts two options, one to control the pitch (available options: 'lowest', 'low', 'med', 'high')
and one to control the output file
```sh
$ py animalese_generator/main.py -m "the quick brown fox jumps over the lazy dog" --pitch high --out output_name.wav
```


## Technologies
Project is created with:
* pydub (need to switch towards pyaudio, because pydub lib isn't being updated for 2 years and their `utils.py` doesn't have propperly escaped regexes)
* click

## Installing required dependencies
```sh
$ pip install pydub
```
[You'll also need to install `ffmpeg` or `libav` for this to work](https://github.com/jiaaro/pydub#dependencies)
```sh
$ brew install ffmpeg
```
or
```sh
$ brew install libav
```
