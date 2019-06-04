from Viewer.mainWindow import *
# from setDialogcontroller import *
from Controller.setParametersDialogcontroller import *
from Controller.encodeDialogcontroller import *
from Controller.errorDialogcontroller import *
from Model import *

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)

        self.model = Model()

        self.setDialog = setDialog(self.model)
        self.actionSet_H264_parameters.triggered.connect(self.setDialog.show)
        self.setDialog.buttonBox.accepted.connect(self.updatePara)

        self.errorDialog = errorDialog()

        self.encodeDialog = encodeDialog()

        self.actionBeginEncode.triggered.connect(self.encodeDialog.show)

        self.encodeDialog.buttonBox.accepted.connect(self.encodeVideo)

    def updatePara(self):
        val_crf = self.setDialog.getCRF()
        self.model.updatePara('crf', val_crf)
        val_qp = self.setDialog.getQP()
        self.model.updatePara('qp', val_qp)
        val_b = self.setDialog.getBitRate()
        self.model.updatePara('b', val_b)
        val_br_method = self.setDialog.getBitControllMethod()
        val_br_method = getElementFromBR_TABLE(val_br_method)
        self.model.updatePara('br_method', val_br_method)
        val_r = self.setDialog.getFrameRate()
        self.model.updatePara('r', val_r)
        val_preset = self.setDialog.getPreset()
        val_preset = getElementFromePRESET_TABLE(val_preset)
        self.model.updatePara('preset', val_preset)
        val_tune = self.setDialog.getTune()
        val_tune = getElementFromeTUNE_TABLE(val_tune)
        self.model.updatePara('tune', val_tune)
        val_deblock = self.setDialog.getDeblock()
        self.model.updatePara('deblock', val_deblock)
        val_deblockalpha = self.setDialog.getDeblockAlpha()
        self.model.updatePara('deblockalpha', val_deblockalpha)
        val_deblockbeta = self.setDialog.getDeblockBeta()
        self.model.updatePara('deblockbeta', val_deblockbeta)
        val_keyint_min = self.setDialog.getIDRMin()
        self.model.updatePara('keyint_min', val_keyint_min)
        val_g = self.setDialog.getIDRMax()
        self.model.updatePara('g', val_g)
        val_ref = self.setDialog.getRefFrame()
        self.model.updatePara('refs', val_ref)
        val_bf = self.setDialog.getBFrame()
        self.model.updatePara('bf', val_bf)
        val_sc_threshold = self.setDialog.getSceneCut()
        self.model.updatePara('sc_threshold', val_sc_threshold)
        val_b_adapt = self.setDialog.getBAdapt()
        self.model.updatePara('b_adapt', val_b_adapt)

    def encodeVideo(self):
        try:
            self.updateFilename()
            self.updateOutput()
            flag = True
        except (type_exc.PathIsEmpty, type_exc.FileAlreadyExists, type_exc.PathNotExists) as e:
            flag = False
            self.errorDialog.errorTypeChanged(e)
            self.errorDialog.exec_()

        if flag:
            self.model.encodeVideo()

    def updateFilename(self):
        self.model.updateFilename(self.fileName)
        # try:
        #     self.model.updateFilename(self.fileName)
        # except type_exc.PathIsEmpty as e:
        #     self.errorDialog.accepted.connect(self.show)
        #     self.errorDialog.errorTypeChanged(e)
        #     self.errorDialog.exec_()

    def updateOutput(self):
        self.model.updateOutput(self.encodeDialog.output)
        # try:
        #     self.model.updateOutput(self.encodeDialog.output)
        # except (type_exc.FileAlreadyExists,  type_exc.PathNotExists) as e:
        #     self.errorDialog.accepted.connect(self.setDialog.show)
        #     self.errorDialog.errorTypeChanged(e)
        #     self.errorDialog.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()

    sys.exit(app.exec_())