import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from vievs.viev import View
#from Model.modulVideo import modulVideo
from PyQt5.QtGui import QPixmap

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        #self._model = modulVideo()
        self._view = View()
        self.init()
########################################
    def init(self):
        pass
        self._view.onClick.connect(self.onClickButton)
        self._view.buttonDialogProjectorSignal.connect(self.buttonDialogProjector)
        self._view.buttonDialogProjectorSignalAccepted.connect(self.buttonDialogProjectorAccepted)
        self._view.buttonDialogScreen_3Signal.connect(self.buttonDialogScreen_3)
        self._view.buttonDialogScreen_2Signal.connect(self.buttonDialogScreen_2)
        self._view.buttonDialogScreen_1Signal.connect(self.buttonDialogScreen_1)
        self._view.OffAllScreenSignal.connect(self.OffAllScreen)
        self._view.OnAllScreenSignal.connect(self.OnAllScreen)
        self._view.buttonDialogScreen_3SignalAccepted.connect(self.buttonDialogScreen_3Accepted)
        self._view.buttonDialogScreen_2SignalAccepted.connect(self.buttonDialogScreen_2Accepted)
        self._view.buttonDialogScreen_1SignalAccepted.connect(self.buttonDialogScreen_1Accepted)
        #self._view.stopButtonSignal.connect(self.buttonStop)

        #self._model.frameSignal.connect(self.test, QtCore.Qt.QueuedConnection)

    def onClickButton(self):
        print("onClickButton")

    def buttonDialogProjector(self):
        print("buttonDialogProjector")

    def buttonDialogProjectorAccepted(self):
            print("buttonDialogProjector1")
    def buttonDialogScreen_3(self):
        print("buttonDialogScreen_3")
    def buttonDialogScreen_2(self):
        print("buttonDialogScreen_2")
    def buttonDialogScreen_1(self):
        print("buttonDialogScreen_1")

    def buttonDialogScreen_3Accepted(self):
            print("buttonDialogScreen_3Accepted")

    def buttonDialogScreen_2Accepted(self):
            print("buttonDialogScreen_2Accepted")

    def buttonDialogScreen_1Accepted(self):
            print("buttonDialogScreen_1Accepted")
    def OffAllScreen(self):
        print("OffAllScreen")
    def OnAllScreen(self):
        print("OnAllScreen")
######################################################
    def run(self):
        self._view.show()
        return self._app.exec_()
