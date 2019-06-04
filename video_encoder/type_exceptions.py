import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class InvalidInput(Exception):
    pass


class InputExceed(Exception):
    pass


class FileAlreadyExists(Exception):
    pass


class PathIsEmpty(Exception):
    pass


class PathNotExists(Exception):
    pass
