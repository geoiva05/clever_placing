from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from registration_Teacher import Registration_Teacher
from forms.registration_Student import Registration_Student


class Check_teacher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('data/check.ui', self)
        self.center()

        self.btn_like_student.clicked.connect(self.regist_like_student)
        self.btn_like_teacher.clicked.connect(self.regist_like_teacher)
        self.btn_back.clicked.connect(self.back)

    def regist_like_student(self):
        self.reg = Registration_Student()
        self.reg.show()

    def regist_like_teacher(self):
        self.reg = Registration_Teacher()
        self.reg.show()

    def back(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
