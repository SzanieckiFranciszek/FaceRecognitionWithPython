from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt, QThread
import numpy as np
import sys
import cv2

face_cascade = cv2.CascadeClassifier('cascade_classifier/haarcascade_frontalface_default.xml')


class CamStartFaceDetection(QThread):
    signal = pyqtSignal(np.ndarray)

    def run(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret, frame = camera.read()
            self.currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_detect = face_cascade.detectMultiScale(self.currentFrame, scaleFactor=1.5, minNeighbors=5)
            for (x1, y1, x2, y2) in face_detect:
                x_for_rectangle = x1 + x2
                y_for_rectangle = y1 + y2
                cv2.rectangle(frame, (x1, y2), (x_for_rectangle, y_for_rectangle), (0, 255, 0), 2)
            if ret:
                self.signal.emit(frame)


class CamDetection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Detection - Cam")
        self.width = 750
        self.height = 600
        self.image = QLabel(self)
        self.image.resize(self.width, self.height)
        self.image.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.cam_start_and_detection = CamStartFaceDetection()
        self.cam_start_and_detection.signal.connect(self._video_update)
        self.cam_start_and_detection.start()

    def _video_update(self, video_cv):
        after_convert = self._convert_to_qt_format(video_cv)
        self.image.setPixmap(after_convert)

    def _convert_to_qt_format(self, video_cv):
        image_rgb_before_convert = cv2.cvtColor(video_cv, cv2.COLOR_BGR2RGB)
        h, w, ch = image_rgb_before_convert.shape
        bytes = ch * w
        convert_to_qt = QtGui.QImage(image_rgb_before_convert.data, w, h, bytes, QtGui.QImage.Format_RGB888)
        image_rgb_after_convert = convert_to_qt.scaled(self.width, self.height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(image_rgb_after_convert)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    cam_detection = CamDetection()
    cam_detection.show()
    sys.exit(application.exec_())
