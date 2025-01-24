"""Test script for Whisper Dictation Mac."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Whisper Dictation Test")
    window.setGeometry(100, 100, 400, 200)
    
    label = QLabel("Whisper Dictation Test Window", window)
    label.setGeometry(50, 80, 300, 40)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 