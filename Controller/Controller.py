import sys
from PyQt5 import QtWidgets

from vievs.viev import View
from Model.SocketServer import Server
from tune_up.settings import Settings


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        pathSettings = r'tune_up/settings'
        self.testSettings = Settings(pathSettings)
        self._view = View()
        self.objServer = Server(self.testSettings)
        self.objServer.start()

        self.init()

    def init(self):
        self._view.onMonitor1Signal.connect(self.pushButtonM1Yes)
        self._view.onMonitor2Signal.connect(self.pushButtonM2Yes)
        self._view.onMonitor3Signal.connect(self.pushButtonM3Yes)
        self._view.offMonitor1Signal.connect(self.pushButtonM1No)
        self._view.offMonitor2Signal.connect(self.pushButtonM2No)
        self._view.offMonitor3Signal.connect(self.pushButtonM3No)
        self._view.onProjectorSignal.connect(self.pushButtonOn)
        self._view.offProjectorSignal.connect(self.pushButtonOff)
        self._view.onAllMonitorSignal.connect(self.pushButtonAllMOn)
        self._view.offAllMonitorSignal.connect(self.pushButtonAllMOff)
        self._view.stopSignal.connect(self.pushStop)

    def pushButtonOn(self):
        if self.objServer.run_projector() == 0:
            self._view.Error_Connection()
        else:
            print("Проектор включён")


    def pushButtonOff(self):
        if self.objServer.stop_projector() == 0:
            self._view.Error_Connection()
        else:
            print("Проектор выключен")

    def pushButtonM1Yes(self):
        if self.objServer.run_monitor1() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №1 включён")

    def pushButtonM1No(self):
        if self.objServer.stop_monitor1() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №1 выключен")

    def pushButtonM2Yes(self):
        if self.objServer.run_monitor2() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №2 включён")

    def pushButtonM2No(self):
        if self.objServer.stop_monitor2() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №2 выключен")


    def pushButtonM3Yes(self):
        if self.objServer.run_monitor3() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №3 включён")


    def pushButtonM3No(self):
        if self.objServer.stop_monitor3() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №3 выключен")

    def pushButtonAllMOn(self):
        if self.objServer.run_video() == 0:
            self._view.Error_Connection()
        else:
            print("Все мониторы включены")


    def pushButtonAllMOff(self):
        if self.objServer.stop_video() == 0:
            self._view.Error_Connection()
        else:
            print("Все мониторы выключены")

    def pushStop(self):
        self.objServer.stop()

    def run(self):
        self._view.show()
        return self._app.exec_()
