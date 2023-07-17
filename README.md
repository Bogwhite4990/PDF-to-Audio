# PDF to Speech Converter

This is a Python script that allows you to convert text from a PDF file to speech using the `gTTS` (Google Text-to-Speech) library. It utilizes the `PyPDF2` library to extract text from the PDF file and the `gTTS` library to generate the speech output. The converted speech output is saved as an audio file and can be played back.

## Installation

To use this script, you need to install the following dependencies:

- `PyPDF2`: You can install it using pip with the command: `pip install PyPDF2`
- `gTTS`: You can install it using pip with the command: `pip install gtts`

## Usage

1. Import the necessary libraries:

```python
import PyPDF2
from gtts import gTTS
import os
