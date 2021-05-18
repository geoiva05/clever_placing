import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class clever_placing(QMainWindow):
    def __init__(self):
        super().__init__()
        self.polz = sqlite3.connect("data/project.db")
        self.cur = self.polz.cursor()
        uic.loadUi('data/sth.ui', self)
        self.initUI()

    def initUI(self):
        pass