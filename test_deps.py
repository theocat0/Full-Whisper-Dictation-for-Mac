import whisper
import sounddevice
import keyboard
import pyperclip
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Whisper Dictation Test")
    window.setGeometry(100, 100, 400, 200)
    
    label = QLabel("Whisper Dictation Test Window")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.setCentralWidget(label)
    
    window.show()
    app.exec()

if __name__ == "__main__":
    main() 