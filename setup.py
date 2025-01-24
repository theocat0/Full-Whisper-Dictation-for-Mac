"""Setup script for Whisper Dictation Mac."""

from setuptools import setup

APP = ['test_deps.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
    'plist': {
        'CFBundleName': 'Whisper Dictation Test',
        'CFBundleDisplayName': 'Whisper Dictation Test',
        'CFBundleIdentifier': 'com.whisperdictation.test',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'LSMinimumSystemVersion': '10.10'
    }
}

setup(
    name='whisper-dictation-mac-test',
    version='0.1.0',
    setup_requires=['py2app'],
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS}
) 