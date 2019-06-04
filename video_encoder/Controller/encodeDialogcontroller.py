import sys
from PyQt5.QtWidgets import *
from Viewer.encodeDialog import *

class encodeDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(encodeDialog, self).__init__(parent)
        self.setupUi(self)
        self.output = None
        self.buttonBox.accepted.connect(self.getOutput)

    def getOutput(self):
        self.output = self.lineEdit.text()
        # print(os.path.exists(self.output))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = encodeDialog()
    myWin.show()
    sys.exit(app.exec_())