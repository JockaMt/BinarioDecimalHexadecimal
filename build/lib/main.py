from imports import *
from mainWindow import mainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec())
