import sys

from PyQt5 import QtGui, QtCore, uic, QtWidgets


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, template):
        super(MyWindow, self).__init__()
        uic.loadUi(template, self)
        self.video = videoThread("192.168.1.150")
        self.video.start()
        self.label.connect(self.video, QtCore.SIGNAL('newImage(QImage)'), self.setFrame)
        self.statusBar().hide()

    def setFrame(self, frame):
        pixmap = QtGui.QPixmap.fromImage(frame)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow('C:\Users\admin\Desktop\Project\Exhibition\vievs\maintesr1.ui')
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())
