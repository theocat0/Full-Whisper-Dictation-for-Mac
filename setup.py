"""Setup script for Whisper Dictation Mac."""

from setuptools import setup

APP = ['src/main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6', 'whisper', 'numpy', 'sounddevice', 'keyboard', 'pyperclip', 'scipy'],
    'plist': {
        'CFBundleName': 'Whisper Dictation',
        'CFBundleDisplayName': 'Whisper Dictation',
        'CFBundleIdentifier': 'com.whisperdictation.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSMinimumSystemVersion': '10.10',
        'NSMicrophoneUsageDescription': 'Microphone access is required for speech recognition.',
        'NSAppleEventsUsageDescription': 'Apple Events are used for keyboard shortcuts.',
    }
}

setup(
    name='whisper-dictation-mac',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'openai-whisper>=0.0.1',
        'PyQt6>=6.4.0',
        'numpy>=1.24.1',
        'sounddevice>=0.4.6',
        'keyboard>=0.13.5',
        'pyperclip>=1.8.2',
        'scipy>=1.10.0'
    ],
) 