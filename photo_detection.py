import sys

import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import *

from photo_detection_ui import Ui_PhotoDetectionWindow

face_cascade = cv2.CascadeClassifier('cascade_classifier/haarcascade_frontalface_default.xml')


class PhotoFaceDetection(QDialog, Ui_PhotoDetectionWindow):
    def __init__(self):
        super(PhotoFaceDetection, self).__init__()
        self._init_photo_detection_ui()
        self.pushButton.clicked.connect(self._get_file_to_detection)
        self.pushButton_2.clicked.connect(self._back_click)

    def _init_photo_detection_ui(self):
        self.setupPhotoUi(self)

    def _format_photo_to_QImage(self, photo_to_format):
        height, width, channel = photo_to_format.shape
        bytes_photo = 3 * width
        image_after_format_to_QImage = QImage(photo_to_format.data, width, height, bytes_photo, QImage.Format_BGR888)
        return image_after_format_to_QImage

    def _get_file_to_detection(self):
        file_name = QFileDialog.getOpenFileName(self, "Open Photo", "c:\\gui\\",
                                                "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        if file_name:

            photo_with_detection = cv2.imread(file_name[0])
            gray = cv2.cvtColor(photo_with_detection, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x1, y1, x2, y2) in faces:
                cv2.rectangle(photo_with_detection, (x1, y1), (x1 + x2, y1 + y2), (0, 255, 0), 2)
            self.photo_after_format = self._format_photo_to_QImage(photo_with_detection)
            self.pixmap = QPixmap.fromImage(self.photo_after_format)
            self.label.setPixmap(self.pixmap)

    def _back_click(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    photo_detection = PhotoFaceDetection()
    photo_detection.show()
    sys.exit(app.exec_())
