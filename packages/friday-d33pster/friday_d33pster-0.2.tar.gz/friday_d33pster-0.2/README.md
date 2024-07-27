# Overview

`Friday` is an AI assistant inspired from Tony Stark's replacement of Vision. `Friday` uses [`vosk model`](https://alphacephei.com/vosk/models) for speech recognition and a custom Natural Language Processing Server that runs in the local host, to identify commands.

`Friday` can also speak, which is done using a custom library written in rust (using [tts_rust](https://crates.io/crates/tts_rust) crate), making use of `GTTS` (Google Text to Speech) client. The rust lib is integrated into python with [`maturin`](https://pypi.org/project/maturin/).

## Table of Contents

- [Mechanism](#mechanism)
- [Requirements](#requirements) (`Manadatory`)
- [Installation](#installation)
- [Usage](#usage)

## Mechanism

- ### Speech to Text

  - `Friday` needs a `vosk model` to recognize speech and convert it to text. `Friday` particularly uses Indian english version of the model. Find it [here](https://alphacephei.com/vosk/models) along with several other versions of `vosk`.

  - The output from `vosk` is processed by a custom NLP server running in the local host, that returns the properly processed command back to `Friday`. This NLP server has been made using rasa platform.

  - Both `vosk model` and `NLP server` are part of `Friday`'s **_"Brain"_** and are a vital part of `Friday`'s response.

- ### Text to Speech

  - `Friday`'s speaking abilities are powered by `Google Text To Speech` client, which was used to write `Friday`'s TTS library in rust (for speed).

  - Apart from that, `Friday` uses threads to speak, which further enhances `Friday`'s voice control.

- ### Overall Integration

  - `Friday`'s overall integration is a result of simultaneous working of several components altogether.

## Requirements

- `Mandatory` [conda](https://docs.anaconda.com/miniconda/miniconda-install/)

  > `conda` must be installed in the system and enabled.

- `Mandatory` [python v3.12](https://www.python.org/downloads/)

  > `rasa` uses python v3.9 and it will be installed in a separate conda env automatically by `Friday`

- `Mandatory` [maturin](https://pypi.org/project/maturin/)

  > can be installed using `$ pip install maturin`

- ffmpeg

  > `ffmpeg` is not a mandatory requirement but if `Friday` encounters some errors related to it, download it.

## Installation

To install `Friday`, clone this repository.

```bash
git clone https://github.com/d33pster/Friday.git
```

then, move into the directory with `cd`.

```bash
cd Friday
```

then, install it using pip.

> `maturin` needs to be installed before this step.

```bash
pip install .
```

## Usage

To use `Friday`, open two terminals.

> in terminal 1

```bash
friday server
```

and wait for it show, `rasa server is up and running!`

> after that, in terminal 2

```bash
friday
```

> After `Friday` is online, just call "Friday!" to wake `Friday` up. and then a command.