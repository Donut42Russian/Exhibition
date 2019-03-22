import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

from Controller.Controller import Controller

def main():
    contro = Controller()
    contro.run()

if __name__ == '__main__':
    sys.exit(main())