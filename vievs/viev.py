import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
#from vievs.MainForm import Ui_MainWindow
from vievs.MainForm import Ui_MonitorManagment


class View(QtWidgets.QMainWindow, Ui_MonitorManagment):

    # startButtonSignal = QtCore.pyqtSignal()

    onClick = QtCore.pyqtSignal()

    onMonitor1Signal = QtCore.pyqtSignal()# Включить монитор №1

    onMonitor2Signal = QtCore.pyqtSignal()# Включить монитор №2

    onMonitor3Signal = QtCore.pyqtSignal()# Включить монитор №3

    offMonitor1Signal = QtCore.pyqtSignal()  # Выключить монитор №1

    offMonitor2Signal = QtCore.pyqtSignal()  # Выключить монитор №2

    offMonitor3Signal = QtCore.pyqtSignal()  # Выключить монитор №3

    onAllMonitorSignal = QtCore.pyqtSignal()# Включить все мониторы

    offAllMonitorSignal = QtCore.pyqtSignal()  # Выключить все мониторы

    onProjectorSignal = QtCore.pyqtSignal() # Включить пректор

    offProjectorSignal = QtCore.pyqtSignal()  # Выключить пректор

    openOptions = QtCore.pyqtSignal() # Открыть параметры

    sendDmitriyMessage = QtCore.pyqtSignal() # Отправить Дмитрию сообщение

    #playVideoSignalForMonitor1 = QtCore.pyqtSignal() # Запустить видео на мониторе №1

    #playVideoSignalForMonitor2 = QtCore.pyqtSignal()  # Запустить видео на монитрое №2

    #playVideoSignalForMonitor3 = QtCore.pyqtSignal()  # Запустить видео на мониторе №3

    #stopVideoSignal = QtCore.pyqtSignal() # Остановить видео

    #selectFoldertoOpenImagesSignal = QtCore.pyqtSignal() # Выбор папки для открытия изобржений



    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''
        self.text1 = ''

        self.initUi()


    def initUi(self):
        pass
        # ##  Кнопки управления
        # self.pushButton.clicked.connect(self.startButtonSignal)

        self.pushButtonM1Yes.clicked.connect(self.onMonitor1Signal)
        self.pushButtonM1No.clicked.connect(self.offMonitor1Signal)
        self.pushButtonM2Yes.clicked.connect(self.onMonitor2Signal)
        self.pushButtonM2No.clicked.connect(self.offMonitor2Signal)
        self.pushButtonM3Yes.clicked.connect(self.onMonitor3Signal)
        self.pushButtonM3No.clicked.connect(self.offMonitor3Signal)
        self.pushButtonOn.clicked.connect(self.onProjectorSignal)
        self.pushButtonOff.clicked.connect(self.offProjectorSignal)
        self.pushButtonAllMOn.clicked.connect(self.onAllMonitorSignal)
        self.pushButtonAllMOff.clicked.connect(self.offAllMonitorSignal)

       #self.pushButtonM1Yes.clicked.connect(self.onMonitor1Signal)
        #self.lineEdit.textChanged.connect(partial(setattr, self, "text"))


        #
        # ## Поля для ввода информации
        # self.spinBox.valueChanged.connect(partial(setattr, self, "minIntensity"))
        # self.spinBox_2.valueChanged.connect(partial(setattr, self, "maxIntensity"))
        # self.spinBox_3.valueChanged.connect(partial(setattr, self, "stepCador"))
        #
        #
        # ## меню
        #self.action.triggered.connect(self.openOptions)
        #self.menu_2.triggered.connect(self.sendDmitryMessage)
        # self.action_LOG.triggered.connect(self.SaveLog)





