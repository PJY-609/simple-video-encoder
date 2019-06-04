import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Viewer.setParameters import *
from Para import *

class setDialog(QDialog, Ui_Dialog):
    def __init__(self, Model, parent=None):
        super(setDialog, self).__init__(parent)
        self.setupUi(self)
        self._CRF = Model.getPara('crf')
        self._QP = Model.getPara('qp')
        self._bitRate = Model.getPara('b')
        self._bitControllMethod = Model.getPara('br_method')
        self._frameRate = Model.getPara('r')
        self._preset = Model.getPara('preset')
        self._tune = Model.getPara('tune')
        self._deblock = Model.getPara('deblock')
        self._deblockBeta = Model.getPara('deblockbeta')
        self._deblockAlpha = Model.getPara('deblockalpha')
        self._IDRMin = Model.getPara('keyint_min')
        self._IDRMax = Model.getPara('g')
        self._refFrame = Model.getPara('refs')
        self._sceneCut = Model.getPara('sc_threshold')
        self._bFrame = Model.getPara('bf')
        self._bAdapt = Model.getPara('b_adapt')

        self.spinBoxCRF.setValue(self._CRF)
        self.spinBoxQP.setValue(self._QP)
        self.spinBoxBitRate.setValue(self._bitRate)
        self.comboBoxBitControllMethod.setCurrentIndex(getIndexFromBR_TABLE(self._bitControllMethod))
        self.spinBoxFrameRate.setValue(self._frameRate)
        self.comboBoxPreset.setCurrentIndex(getIndexFromPRESET_TABLE(self._preset))
        self.comboBoxTune.setCurrentIndex(getIndexFromTUNE_TABLE(self._tune))
        self.comboBoxDeblock.setCurrentIndex(self._deblock)
        self.spinBoxDeblockAlpha.setValue(self._deblockAlpha)
        self.spinBoxDeblockBeta.setValue(self._deblockBeta)
        self.spinBoxIDRMin.setValue(self._IDRMin)
        self.spinBoxIDRMax.setValue(self._IDRMax)
        self.spinBoxSceneCut.setValue(self._sceneCut)
        self.spinBoxBFrame.setValue(self._bFrame)
        self.spinBoxRefFrame.setValue(self._refFrame)
        self.comboBoxBAdapt.setCurrentIndex(self._bAdapt)

        self.buttonBox.accepted.connect(self.updateCRF)
        self.buttonBox.accepted.connect(self.updateQP)
        self.buttonBox.accepted.connect(self.updateBitRate)
        self.buttonBox.accepted.connect(self.updateBitControllMethod)
        self.buttonBox.accepted.connect(self.updateFrameRate)
        self.buttonBox.accepted.connect(self.updatePreset)
        self.buttonBox.accepted.connect(self.updateTune)
        self.buttonBox.accepted.connect(self.updateDeblock)
        self.buttonBox.accepted.connect(self.updateDeblockAlpha)
        self.buttonBox.accepted.connect(self.updateDeblockBeta)
        self.buttonBox.accepted.connect(self.updateIDRMax)
        self.buttonBox.accepted.connect(self.updateIDRMin)
        self.buttonBox.accepted.connect(self.updateRefFrame)
        self.buttonBox.accepted.connect(self.updateSceneCut)
        self.buttonBox.accepted.connect(self.updateBFrame)
        self.buttonBox.accepted.connect(self.updateBAdapt)

    def updateCRF(self):
        self._CRF = self.spinBoxCRF.value()
        self.spinBoxCRF.setValue(self._CRF)

    def updateQP(self):
        self._QP = self.spinBoxQP.value()
        self.spinBoxQP.setValue(self._QP)

    def updateBitRate(self):
        self._bitRate = self.spinBoxBitRate.value()
        self.spinBoxBitRate.setValue(self._bitRate)

    def updateBitControllMethod(self):
        self._bitControllMethod = self.comboBoxBitControllMethod.currentIndex()
        self.comboBoxBitControllMethod.setCurrentIndex(self._bitControllMethod)

    def updateFrameRate(self):
        self._frameRate = self.spinBoxFrameRate.value()
        self.spinBoxFrameRate.setValue(self._frameRate)

    def updatePreset(self):
        self._preset = self.comboBoxPreset.currentIndex()
        self.comboBoxPreset.setCurrentIndex(self._preset)

    def updateTune(self):
        self._tune = self.comboBoxTune.currentIndex()
        self.comboBoxTune.setCurrentIndex(self._tune)

    def updateDeblock(self):
        self._deblock = self.comboBoxDeblock.currentIndex()
        self.comboBoxDeblock.setCurrentIndex(self._deblock)

    def updateDeblockAlpha(self):
        self._deblockAlpha = self.spinBoxDeblockAlpha.value()
        self.spinBoxDeblockAlpha.setValue(self._deblockAlpha)

    def updateDeblockBeta(self):
        self._deblockBeta = self.spinBoxDeblockBeta.value()
        self.spinBoxDeblockBeta.setValue(self._deblockBeta)

    def updateIDRMax(self):
        self._IDRMax = self.spinBoxIDRMax.value()
        self.spinBoxIDRMax.setValue(self._IDRMax)

    def updateIDRMin(self):
        self._IDRMin = self.spinBoxIDRMin.value()
        self.spinBoxIDRMin.setValue(self._IDRMin)

    def updateRefFrame(self):
        self._refFrame = self.spinBoxRefFrame.value()
        self.spinBoxRefFrame.setValue(self._refFrame)

    def updateSceneCut(self):
        self._sceneCut = self.spinBoxSceneCut.value()
        self.spinBoxSceneCut.setValue(self._sceneCut)

    def updateBFrame(self):
        self._bFrame = self.spinBoxBFrame.value()
        self.spinBoxBFrame.setValue(self._bFrame)

    def updateBAdapt(self):
        self._bAdapt = self.comboBoxBAdapt.currentIndex()
        self.comboBoxBAdapt.setCurrentIndex(self._bAdapt)

    def getCRF(self):
        return self._CRF

    def getQP(self):
        return self._QP

    def getBitRate(self):
        return self._bitRate

    def getBitControllMethod(self):
        return self._bitControllMethod

    def getFrameRate(self):
        return self._frameRate

    def getPreset(self):
        return self._preset

    def getTune(self):
        return self._tune

    def getDeblock(self):
        return self._deblock

    def getDeblockBeta(self):
        return self._deblockBeta

    def getDeblockAlpha(self):
        return self._deblockAlpha

    def getIDRMax(self):
        return self._IDRMax

    def getIDRMin(self):
        return self._IDRMin

    def getRefFrame(self):
        return self._refFrame

    def getSceneCut(self):
        return self._sceneCut

    def getBFrame(self):
        return self._bFrame

    def getBAdapt(self):
        return self._bAdapt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = setDialog()
    myWin.show()
    sys.exit(app.exec_())
