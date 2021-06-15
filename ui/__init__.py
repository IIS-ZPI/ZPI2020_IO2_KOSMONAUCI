import sys

from PyQt5 import QtWidgets

from ui import main


class MainQtWindow(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainQtWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MainQtWindow()
    qt_app.show()
    app.exec()
