# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from setH264Parameters import *

class Ui_MainWindow(object):
    def __init__(self):
        self.fileName = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 593)

        self.wid = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.wid)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoWidget = QVideoWidget(MainWindow)
        self.videoWidget.setObjectName("videoWidget")
        self.playButton = QtWidgets.QPushButton(MainWindow)
        # self.playButton.setGeometry(QtCore.QRect(0, 540, 30, 30))
        self.playButton.setIcon(MainWindow.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.playButton.setObjectName("playButton")

        self.positionSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)

        self.controlLayout = QtWidgets.QHBoxLayout()
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.controlLayout.addWidget(self.playButton)
        self.controlLayout.addWidget(self.positionSlider)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.videoWidget)
        self.layout.addLayout(self.controlLayout)

        self.wid.setLayout(self.layout)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuEncode = QtWidgets.QMenu(self.menubar)
        self.menuEncode.setObjectName("menuEncode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSet_H264_parameters = QtWidgets.QAction(MainWindow)
        self.actionSet_H264_parameters.setObjectName("actionSet_H264_parameters")
        self.actionBeginEncode = QtWidgets.QAction(MainWindow)
        self.actionBeginEncode.setObjectName("actionBeginEncode")
        # self.dialog = Ui_Dialog()
        self.menuFile.addAction(self.actionOpen)
        self.menuSettings.addAction(self.actionSet_H264_parameters)
        self.menuEncode.addAction(self.actionBeginEncode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuEncode.menuAction())

        self.actionOpen.triggered.connect(self.openFileDialog)

        self.playButton.setEnabled(False)
        self.playButton.clicked.connect(self.play)

        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.playButton.setText(_translate("MainWindow", "PushButton"))
        # self.pauseButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuEncode.setTitle(_translate("MainWindow", "Encode"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSet_H264_parameters.setText(_translate("MainWindow", "Set H264 parameters"))
        self.actionBeginEncode.setText(_translate("MainWindow", "Begin Encode"))
        # self.positionSlider.setText(_translate("MainWindow", "Slide Position"))

    def openFileDialog(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", "D:", "All Files(*)")

        if self.fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QtCore.QUrl.fromLocalFile(self.fileName)))
            self.playButton.setEnabled(True)
            self.mediaPlayer.play()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)