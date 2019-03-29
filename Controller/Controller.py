import sys
from PyQt5 import QtCore, QtGui, QtWidgets 


from vievs.viev import View 
#from Model.modulVideo import modulVideo
#from PyQt5.QtGui import QPixmap

class Controller: 
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        #self._model = modulVideo()
        self._view = View()
        self.init()

    def init(self):
        self._view.onMonitor1Signal.connect(self.pushButtonM1Yes)
        self._view.onMonitor2Signal.connect(self.pushButtonM2Yes)
        self._view.onMonitor3Signal.connect(self.pushButtonM3Yes)
        #self._view.onClick.connect(self.onClickButton)
        self._view.offMonitor1Signal.connect(self.pushButtonM1No)
        self._view.offMonitor2Signal.connect(self.pushButtonM2No)
        self._view.offMonitor3Signal.connect(self.pushButtonM3No)
        self._view.onProjectorSignal.connect(self.pushButtonOn)
        self._view.offProjectorSignal.connect(self.pushButtonOff)
        self._view.onAllMonitorSignal.connect(self.pushButtonAllMOn)
        self._view.offAllMonitorSignal.connect(self.pushButtonAllMOff)

        #self._view.stopButtonSignal.connect(self.buttonStop)

        #self._model.frameSignal.connect(self.test, QtCore.Qt.QueuedConnection)

    def onClickButton(self):
        print("Проектор включён")
        print(self._view.text)

    def pushButtonM1Yes(self):
        print("Монитор №1 включён")

    def pushButtonM2Yes(self):
        print("Монитор №2 включён")
        #print(self._view.text
    def pushButtonM3Yes(self):
        print("Монитор №3 включён")

    def pushButtonOn(self):
        print("Проектор включён")

    def pushButtonM1No(self):
        print("Монитор №1 выключен")
    def pushButtonM2No(self):
        print("Монитор №2 выключен")

    def pushButtonM3No(self):
        print("Монитор №3 выключен")

    def pushButtonOff(self):
        print("Проектор выключен")

    def pushButtonAllMOn(self):
        print("Все мониторы включены")

    def pushButtonAllMOff(self):
        print("Все мониторы выключены")



    def run(self):
        self._view.show()
        return self._app.exec_()



    def onProjector1(self): #Включить 1 проектор

        print ("Проектор 1 включен")
        #self._view.pushButtonM1Yes.connect(self.onClickButton)






    #def offProjector(self):