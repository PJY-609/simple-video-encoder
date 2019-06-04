import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Viewer.errorDialog import *


class errorDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(errorDialog, self).__init__(parent)
        self.setupUi(self)

    def errorTypeChanged(self, err):
        self.plainTextEdit.clear()
        self.plainTextEdit.insertPlainText("{}".format(err.args[0]))


