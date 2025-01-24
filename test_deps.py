import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Whisper Dictation Test")
    window.setGeometry(100, 100, 400, 200)
    
    label = QLabel("Whisper Dictation Test Window", window)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setGeometry(50, 50, 300, 50)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 