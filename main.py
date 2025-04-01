import sys
from PySide6 import QtWidgets as qtw

from Main import main

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = main.SerialApp()

    window.show()

    sys.exit(app.exec())

