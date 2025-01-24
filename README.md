# Whisper Dictation for Mac

A native macOS dictation application using OpenAI's Whisper model for offline speech recognition, optimized for Apple Silicon (M1/M2).

## Features

- 🎙️ Local speech recognition (no internet required)
- ⌨️ Global hotkey (⌘⇧Space) to start recording
- 📎 Automatic clipboard copy of transcribed text
- 🎯 Optimized for Apple Silicon
- 🔒 100% Private - all processing done locally

## Quick Install

1. Download the latest release from the [Releases](https://github.com/yourusername/whisper-dictation-mac/releases) page
2. Unzip and drag `Whisper Dictation.app` to your Applications folder
3. Launch and grant microphone permissions when prompted

## Build from Source

### Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- Git

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/whisper-dictation-mac.git
cd whisper-dictation-mac

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the application
python setup.py py2app
```

The built application will be in the `dist` folder.

## Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/whisper-dictation-mac.git
cd whisper-dictation-mac

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python src/main.py
```

## Project Structure

```
whisper-dictation-mac/
├── src/
│   ├── whisperdictation/
│   │   ├── __init__.py
│   │   └── app.py
│   └── main.py
├── assets/
│   └── icon.icns
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## Requirements

- macOS 11.0 or later
- Apple Silicon Mac (M1/M2)
- ~2GB disk space (for Whisper model)

## Privacy

- All speech recognition is performed locally on your device
- No audio data is ever sent to external servers
- No telemetry or data collection

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the amazing speech recognition model
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework 