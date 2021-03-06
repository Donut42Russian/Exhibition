from PyQt5 import QtCore, QtWidgets
from vievs.MainForm import Ui_MonitorManagment

from vievs.video import videoThread


class View(QtWidgets.QMainWindow, Ui_MonitorManagment):
    onClick = QtCore.pyqtSignal()

    onMonitor1Signal = QtCore.pyqtSignal()  # Включить монитор №1
    onMonitor2Signal = QtCore.pyqtSignal()  # Включить монитор №2
    onMonitor3Signal = QtCore.pyqtSignal()  # Включить монитор №3
    offMonitor1Signal = QtCore.pyqtSignal()  # Выключить монитор №1
    offMonitor2Signal = QtCore.pyqtSignal()  # Выключить монитор №2
    offMonitor3Signal = QtCore.pyqtSignal()  # Выключить монитор №3
    onAllMonitorSignal = QtCore.pyqtSignal()  # Включить все мониторы
    offAllMonitorSignal = QtCore.pyqtSignal()  # Выключить все мониторы
    onProjectorSignal = QtCore.pyqtSignal()  # Включить пректор
    offProjectorSignal = QtCore.pyqtSignal()  # Выключить пректор
    openOptions = QtCore.pyqtSignal()  # Открыть параметры
    sendDmitriyMessage = QtCore.pyqtSignal()  # Отправить Дмитрию сообщение
    stopSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''
        self.text1 = ''
        self.initUi()

        ico = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay) # Иконка в трее
        self.sys_tray = QtWidgets.QSystemTrayIcon(ico, self)  #

        self.sys_tray.setToolTip("MonitorManagment")  # Текст выходящий при наведении на иконку в трее

        self.sys_tray.activated.connect(self.on_activated)

        self.sys_tray.messageClicked.connect(self.on_messageClicked)
        self.sys_tray.show()

        self.on_create_context_menu()

    def initUi(self):
        self.Video = videoThread('192.168.1.101')
        self.Video.start()

        self.graphicsSceneImage = QtWidgets.QGraphicsScene()
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

        self.Video.frameSignal.connect(self.showGraphicsViewImage, QtCore.Qt.QueuedConnection)

    def showGraphicsViewImage(self, pixMap):
        self.graphicsSceneImage.clear()
        self.graphicsSceneImage.addPixmap(pixMap)
        self.graphicsView.setScene(self.graphicsSceneImage)

    def Error_Connection(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText('Не все клиенты(Raspberry) подключились!')
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.exec_()





    def on_create_context_menu(self):
        self.menuSystemTray = QtWidgets.QMenu("&SystemTray")
        self.actShowHide = QtWidgets.QAction("&Отобразить или скрыть окно", None)
        self.actShowHide.triggered.connect(self.on_show_hide)
        self.menuSystemTray.addAction(self.actShowHide)
        self.menuSystemTray.addSeparator()
        self.actQuit = QtWidgets.QAction("&Выход", None)

        self.actQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actQuit.triggered.connect(self.stopSignal)

        self.menuSystemTray.addAction(self.actQuit)
        self.sys_tray.setContextMenu(self.menuSystemTray)

    def closeEvent(self, e):
        self.hide()
        e.ignore()

    def on_clicked(self):
        self.sys_tray.showMessage("Название", "Текст сообщения", msecs=2000)

    def on_show_hide(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.activateWindow()

    def on_activated(self, st):
        print("on_activated", st)

    def on_messageClicked(self):
        print("on_messageClicked")

