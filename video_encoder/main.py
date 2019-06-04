from Controller.mainWindowcontroller import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()

    sys.exit(app.exec_())