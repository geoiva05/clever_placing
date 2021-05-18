import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from forms.entrance_student import Entrance_Student
from forms.registration_Student import Registration_Student


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class apposition(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Enter_or_regist.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.btn_enter.clicked.connect(self.Entrance)
        self.btn_regist.clicked.connect(self.Regist)

    def Entrance(self):
        self.ch = Entrance_Student()
        self.ch.show()


    def Regist(self):
        self.ch = Registration_Student()
        self.ch.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = apposition()
    ex.show()
    sys.exit(app.exec())
