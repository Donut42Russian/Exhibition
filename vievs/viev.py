import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
#from vievs.MainForm import Ui_MainWindow
from vievs.MainForm import Ui_MonitorManagment


class View(QtWidgets.QMainWindow, Ui_MonitorManagment):

    # startButtonSignal = QtCore.pyqtSignal()

    onClick = QtCore.pyqtSignal()
    buttonDialogProjectorSignal = QtCore.pyqtSignal()
    buttonDialogProjectorSignalAccepted = QtCore.pyqtSignal()
    buttonDialogScreen_3Signal = QtCore.pyqtSignal()
    buttonDialogScreen_3SignalAccepted = QtCore.pyqtSignal()
    buttonDialogScreen_2Signal = QtCore.pyqtSignal()
    buttonDialogScreen_2SignalAccepted = QtCore.pyqtSignal()
    buttonDialogScreen_1Signal = QtCore.pyqtSignal()
    buttonDialogScreen_1SignalAccepted = QtCore.pyqtSignal()
    OffAllScreenSignal = QtCore.pyqtSignal()
    OnAllScreenSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''

        self.initUi()


    def initUi(self):
        pass
        # ##  Кнопки управления
        # self.pushButton.clicked.connect(self.startButtonSignal)

        self.pushButton.clicked.connect(self.onClick)
        self.ProjectorIndicator.clicked.connect(self.onClick)
        self.buttonDialogProjector.accepted.connect(self.buttonDialogProjectorSignalAccepted)
        self.buttonDialogProjector.rejected.connect(self.buttonDialogProjectorSignal)
        self.buttonDialogScreen_3.accepted.connect(self.buttonDialogScreen_3SignalAccepted)
        self.buttonDialogScreen_3.rejected.connect(self.buttonDialogScreen_3Signal)
        self.buttonDialogScreen_2.accepted.connect(self.buttonDialogScreen_2SignalAccepted)
        self.buttonDialogScreen_2.rejected.connect(self.buttonDialogScreen_2Signal)
        self.buttonDialogScreen_1.accepted.connect(self.buttonDialogScreen_1SignalAccepted)
        self.buttonDialogScreen_1.rejected.connect(self.buttonDialogScreen_1Signal)
        #self.ScreenIndicator_3.clicked.connect(self.Signal)
        #self.ScreenIndicator_2.clicked.connect(self.Signal)
        #self.ScreenIndicator_1.clicked.connect(self.Signal)
        self.OffAllScreen.clicked.connect(self.OffAllScreenSignal)
        self.OnAllScreen.clicked.connect(self.OnAllScreenSignal)
        # self.lineEdit.textChanged.connect(partial(setattr, self, "text"))


        #
        # ## Поля для ввода информации
        # self.spinBox.valueChanged.connect(partial(setattr, self, "minIntensity"))
        # self.spinBox_2.valueChanged.connect(partial(setattr, self, "maxIntensity"))
        # self.spinBox_3.valueChanged.connect(partial(setattr, self, "stepCador"))
        #
        #
        # ## меню
        # self.action.triggered.connect(self.openFileVideo)
        # self.action_LOG.triggered.connect(self.SaveLog)





