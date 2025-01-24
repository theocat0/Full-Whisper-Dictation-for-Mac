# Whisper Dictation for macOS

A native macOS application that provides real-time speech-to-text dictation using OpenAI's Whisper model.

## Download and Installation

### Easy Installation (Recommended)
1. Go to the [Releases](https://github.com/yourusername/Dictation_whisper_Mac/releases) page
2. Download the latest `Whisper.Dictation.app.zip` file
3. Unzip the file
4. Move `Whisper Dictation.app` to your Applications folder
5. Double-click to launch the application

Note: When launching for the first time, macOS might show a security warning. To resolve this:
1. Open System Preferences > Security & Privacy
2. Click "Open Anyway" to allow the application to run

### Building from Source
If you prefer to build the application yourself:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Dictation_whisper_Mac.git
cd Dictation_whisper_Mac
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Build the application:
```bash
pyinstaller --name="Whisper Dictation" --windowed --add-data "src:src" --hidden-import=whisperdictation.app src/main.py
```

The built application will be available in the `dist` directory.

## Features

- Real-time speech-to-text transcription
- Uses OpenAI's Whisper model for accurate transcription
- Native macOS application
- Keyboard shortcuts for quick access
- Clipboard integration for easy text pasting

## System Requirements

- macOS 10.10 or later
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

## Usage

1. Launch the application
2. Click the microphone button or use the keyboard shortcut to start recording
3. Speak clearly into your microphone
4. The transcribed text will appear in the application window
5. Click to copy the text to your clipboard

## Known Issues

- First launch may take a few seconds while the Whisper model is loaded
- Requires an active internet connection for initial model download

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the speech recognition model
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework
