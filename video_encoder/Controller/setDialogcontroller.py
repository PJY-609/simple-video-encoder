import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from setH264Parameters import *
import type_exceptions as type_exc

class setDialog(QDialog, Ui_Dialog):
    def __init__(self, Model, parent=None):
        super(setDialog, self).__init__(parent)
        self.setupUi(self)
        self._CRF = Model.getPara('crf')
        self.buttonBox.accepted.connect(self.updateCRF)

    def updateCRF(self):
        self._CRF = self.spinBoxCRF.value()
        self.spinBoxCRF.setValue(self._CRF)

    def getCRF(self):
        return self._CRF


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = setDialog()
    myWin.show()
    sys.exit(app.exec_())