import sys

import cv2
from PyQt5 import QtGui, QtCore, uic, QtWidgets


class videoThread(QtCore.QThread):
    # Requires IP address of streaming server
    def __init__(self):
        super(videoThread, self).__init__()
        self.ip = "192.168.1.101"

    def run(self):
        # Create a capture object using the IP address specified at init.
        cap = cv2.VideoCapture("http://" + str(self.ip) +
                               ":8080/?action=stream?dummy=param.mjpg")
        while cap.isOpened():
            _, frame = cap.read()
            image = QtGui.QImage(frame.tostring(), 1280, 720, QtGui.QImage.Format_RGB888)
            self.emit(QtCore.SIGNAL('newImage(QImage)'), image)


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, template):
        super(MyWindow, self).__init__()
        uic.loadUi(template, self)
        self.video = videoThread("192.168.1.101")
        self.video.start()
        self.label.connect(self.video, QtCore.SIGNAL('newImage(QImage)'), self.setFrame)
        self.statusBar().hide()

    def setFrame(self, frame):
        pixmap = QtGui.QPixmap.fromImage(frame)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow('~vievs/maintesr1.ui')
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())
