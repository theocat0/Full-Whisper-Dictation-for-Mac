import sys
import os
import tempfile
import threading
import keyboard
import pyperclip
import sounddevice as sd
import numpy as np
import whisper
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                           QVBoxLayout, QWidget, QLabel)
from PyQt6.QtCore import Qt, pyqtSignal, QObject

class SignalHandler(QObject):
    transcription_complete = pyqtSignal(str)

class WhisperDictationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.signal_handler = SignalHandler()
        self.recording = False
        self.audio_data = []
        self.sample_rate = 16000
        self.model = None
        self.init_ui()
        self.init_whisper_model()
        self.setup_global_hotkey()

    def init_ui(self):
        self.setWindowTitle('Whisper Dictation')
        self.setGeometry(100, 100, 300, 150)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.status_label = QLabel('Press Cmd+Shift+Space to start recording')
        self.record_button = QPushButton('Stop Recording')
        self.record_button.setEnabled(False)
        
        layout.addWidget(self.status_label)
        layout.addWidget(self.record_button)
        
        self.record_button.clicked.connect(self.stop_recording)
        self.signal_handler.transcription_complete.connect(self.handle_transcription)
        
        # Set window flags to keep it always on top
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def init_whisper_model(self):
        # Load the model in a separate thread to not block the UI
        def load_model():
            self.model = whisper.load_model("base")
            self.status_label.setText('Ready - Press Cmd+Shift+Space to start recording')
        
        threading.Thread(target=load_model, daemon=True).start()

    def setup_global_hotkey(self):
        keyboard.add_hotkey('cmd+shift+space', self.start_recording)

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.audio_data = []
            self.status_label.setText('Recording... Click Stop when done')
            self.record_button.setEnabled(True)
            self.show()
            self.raise_()
            
            # Start recording in a separate thread
            threading.Thread(target=self._record_audio, daemon=True).start()

    def _record_audio(self):
        def callback(indata, frames, time, status):
            if self.recording:
                self.audio_data.append(indata.copy())

        with sd.InputStream(samplerate=self.sample_rate, channels=1, 
                          callback=callback):
            while self.recording:
                sd.sleep(100)

    def stop_recording(self):
        self.recording = False
        self.record_button.setEnabled(False)
        self.status_label.setText('Transcribing...')
        
        # Process audio in a separate thread
        threading.Thread(target=self._process_audio, daemon=True).start()

    def _process_audio(self):
        if not self.audio_data:
            self.signal_handler.transcription_complete.emit("")
            return

        audio = np.concatenate(self.audio_data)
        
        # Save audio to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            import scipy.io.wavfile as wavfile
            wavfile.write(temp_audio.name, self.sample_rate, audio)
            
            # Transcribe using Whisper
            result = self.model.transcribe(temp_audio.name)
            
        # Clean up temporary file
        os.unlink(temp_audio.name)
        
        self.signal_handler.transcription_complete.emit(result["text"].strip())

    def handle_transcription(self, text):
        if text:
            pyperclip.copy(text)
            keyboard.write(text)
        self.hide()
        self.status_label.setText('Ready - Press Cmd+Shift+Space to start recording')

def main():
    app = QApplication(sys.argv)
    window = WhisperDictationApp()
    sys.exit(app.exec()) 