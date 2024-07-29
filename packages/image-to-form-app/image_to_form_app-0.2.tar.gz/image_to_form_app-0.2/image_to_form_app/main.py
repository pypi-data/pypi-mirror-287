import sys
from PyQt5.QtWidgets import QApplication
from .gui import ImageUploaderApp

def main():
    app = QApplication(sys.argv)
    ex = ImageUploaderApp()
    ex.show()
    sys.exit(app.exec_())
