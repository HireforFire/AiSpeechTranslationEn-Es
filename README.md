# Speech Translation with Text-to-Speech

This repository contains a Python script that demonstrates speech translation using the `speech_recognition`, `transformers`, `MarianMTModel`, `MarianTokenizer`, `pyttsx3`, and `langdetect` libraries. The script allows you to speak in either English or Spanish, and it will translate your speech to the other language while also providing an audible response.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.6 or higher
- `speech_recognition` library: This library provides easy access to the Google Web Speech API for speech recognition.
- `transformers` library: This library provides access to the `MarianMTModel` and `MarianTokenizer` for machine translation.
- `pyttsx3` library: This library allows text-to-speech functionality to provide audible translations.
- `langdetect` library: This library is used to automatically detect the language spoken by the user.

You can install the required packages using pip:

```bash
pip install SpeechRecognition transformers pyttsx3 langdetect
```

## Usage

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/speech-translation.git
```

2. Change into the project directory.

```bash
cd speech-translation
```

3. Run the Python script.

```bash
python speech_translation.py
```

4. Speak into your computer's microphone when prompted. The script will detect the language you spoke in and translate it to the other language.

## How it Works

The script initializes recognizer objects for speech recognition and tokenizer and model objects for machine translation using the `transformers` library. It also sets up a text-to-speech engine using `pyttsx3`.

The main loop continuously listens to your speech input using the default microphone as the audio source. It then uses Google Speech Recognition to convert the speech to text. The script detects the language of the input using `langdetect`.

If the detected language is Spanish (`es`), the script translates the input text to English using the pre-trained `MarianMTModel` and `MarianTokenizer` for Spanish to English translation. The translated text is then spoken out loud using the text-to-speech engine.

If the detected language is English (`en`), the script translates the input text to Spanish using the pre-trained `MarianMTModel` and `MarianTokenizer` for English to Spanish translation. Again, the translated text is spoken using the text-to-speech engine.

If the detected language is neither English nor Spanish, the script will display an "Unsupported language" message.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

---

Happy speech translation and text-to-speech! If you encounter any issues or have any questions, please don't hesitate to reach out.

*Note: This readme assumes that you have access to the required pre-trained models for machine translation provided by the `transformers` library. If not, make sure you have internet access during the first run of the script to download the necessary model files.*Ai 
