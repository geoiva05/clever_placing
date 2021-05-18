from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from forms.entrance_student import Entrance_Student
from entrance_teacher import Entrance_Teacher


class Check_entrance(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('data/check.ui', self)
        self.center()
        self.btn_like_teacher.setText('Войти как учитель')
        self.btn_like_student.setText('Войти как ученик')
        self.btn_like_student.clicked.connect(self.entrance_like_student)
        self.btn_like_teacher.clicked.connect(self.entrance_like_teacher)
        self.btn_back.clicked.connect(self.back)

    def entrance_like_teacher(self):
        self.wind = Entrance_Teacher()
        self.wind.show()

    def entrance_like_student(self):
        self.wind = Entrance_Student()
        self.wind.show()

    def back(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
