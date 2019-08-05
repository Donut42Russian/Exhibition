import sys
import qimage2ndarray
import numpy
import cv2
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtGui import QPixmap


class videoThread(QtCore.QThread):
    frameSignal = QtCore.pyqtSignal(QPixmap)
    # Requires IP address of streaming server
    def __init__(self, ip):
        super(videoThread, self).__init__()
        self.ip = ip

    def converterNumpyToPixMap(self, NumpyArray):
        pixMapArray = QPixmap.fromImage(qimage2ndarray.array2qimage(NumpyArray))
        return pixMapArray

    def transvormFrame(self, frame):
        '''
        Транформируем по размеру виждета
        :param frame:
        :return:
        '''

        return frame.scaled(self.withVideoViget, self.heightVideoViget, QtCore.Qt.KeepAspectRatio)

    def run(self):
        # Create a capture object using the IP address specified at init.
        cap = cv2.VideoCapture("http://" + str(self.ip) +
                               ":8080/?action=stream?dummy=param.mjpg")
        while cap.isOpened():
            _, frame = cap.read()
            #image = QtGui.QImage(frame.tostring(), 1280, 720, QtGui.QImage.Format_RGB888)
            #print(type(image))
            self.frameSignal.emit(self.converterNumpyToPixMap(frame))
            print("dasd")
