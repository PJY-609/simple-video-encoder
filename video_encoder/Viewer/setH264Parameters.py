# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setH264Parameters.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 466)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 310, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.hLayoutWidget_1 = QtWidgets.QWidget(Dialog)
        self.hLayoutWidget_1.setGeometry(QtCore.QRect(80, 50, 100, 40))
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCRF= QtWidgets.QLabel(self.hLayoutWidget_1)
        self.labelCRF.setObjectName("labelCRF")
        self.hLayout.addWidget(self.labelCRF)
        self.spinBoxCRF = QtWidgets.QSpinBox(self.hLayoutWidget_1)
        self.spinBoxCRF.setObjectName("lineEditCRF")
        self.spinBoxCRF.setRange(1, 51)
        self.spinBoxCRF.setSingleStep(1)


        self.hLayout.addWidget(self.spinBoxCRF)
        self.hLayoutWidget_1.setLayout(self.hLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelCRF.setText(_translate("Dialog", "CRF"))
        # self.label_3.setText(_translate("Dialog", "分辨率"))
        # self.label_4.setText(_translate("Dialog", "Profile"))
        # self.label_5.setText(_translate("Dialog", "CRF"))
        # self.comboBox.setItemText(0, _translate("Dialog", "Baseline"))
        # self.comboBox.setItemText(1, _translate("Dialog", "Main"))
        # self.comboBox.setItemText(2, _translate("Dialog", "High"))
        # self.comboBox_2.setItemText(0, _translate("Dialog", "Plcaebo"))
        # self.comboBox_2.setItemText(1, _translate("Dialog", "Medium"))
        # self.comboBox_2.setItemText(2, _translate("Dialog", "Ultrafast"))
        # self.label.setText(_translate("Dialog", "帧速率"))
        # self.label_6.setText(_translate("Dialog", "QP"))

