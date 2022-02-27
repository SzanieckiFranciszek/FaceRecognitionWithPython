import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from cam_detection import CamDetection
from main_menu_ui import Ui_Dialog
from photo_detection import PhotoFaceDetection


class MainMenu(QDialog, Ui_Dialog):

    def __init__(self):
        super(MainMenu, self).__init__()
        self._init_main_menu_ui()
        self.pushButton.clicked.connect(self._init_cam_face_detection)
        self.pushButton_2.clicked.connect(self._init_photo_face_detection)

    def _init_main_menu_ui(self):
        self.setupUi(self)

    def _init_cam_face_detection(self):
        self.cam_detection = CamDetection()
        self.cam_detection.show()

    def _init_photo_face_detection(self):
        self.photo_detection = PhotoFaceDetection()
        self.photo_detection.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())
