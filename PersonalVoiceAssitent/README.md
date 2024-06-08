# Voice Assistant with Python and Hugging Face Transformers

## Introduction

This project demonstrates how to build a voice assistant using Python and Hugging Face transformers. The voice assistant can transcribe speech, process queries, and respond with synthesized speech. It leverages state-of-the-art models for automatic speech recognition (ASR), natural language processing (NLP), and text-to-speech (TTS) synthesis.

## Features

- **Speech Recognition:** Transcribes spoken words into text using the `openai/whisper-base.en` model.
- **Natural Language Processing:** Processes the transcribed text and generates a response using the `tiiuae/falcon-7b-instruct` model.
- **Text-to-Speech Synthesis:** Converts the generated response into speech using the `microsoft/speecht5_tts` model and a vocoder.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.6 or higher
- `transformers` library
- `sentencepiece` library
- `datasets` library


## Open the Notebook in Google Colab

1. **Open Google Colab:**
   - Go to [Google Colab](https://colab.research.google.com/).

2. **Open the Notebook from GitHub:**
   - Click on `File` &gt; `Open notebook`.
   - In the dialog that appears, click on the `GitHub` tab.
   - Authenticate with GitHub if prompted.
   - Enter the complete file url and press Enter.

## Run the Notebook

1. **Install Required Libraries:**
   - Ensure that the first cell in your notebook installs all necessary libraries. For example:

   ```python
   !pip install transformers sentencepiece datasets[audio]
   ```

2. **Execute Cells:**
Run each cell in the notebook sequentially to set up and execute your project.


## Note on Using `ffmpeg`

- **Using `ffmpeg` for Audio Input:**
  - we are using `ffmpeg` to capture audio from the microphone, please note that this functionality will not work in Google Colab. Google Colab does not support direct audio input from the microphone.
  - To use `ffmpeg` for capturing audio, you will need to run the notebook on your local machine and install `ffmpeg` locally.

  ### Installing `ffmpeg` Locally:
  - **Windows:**
    1. Download the `ffmpeg` executable from [ffmpeg.org](https://ffmpeg.org/download.html).
    2. Extract the downloaded archive.
    3. Add the `bin` directory of the extracted folder to your system's PATH environment variable.

  - **MacOS:**
    ```sh
    brew install ffmpeg
    ```

  - **Linux:**
    ```sh
    sudo apt-get update
    sudo apt-get install ffmpeg
    ```