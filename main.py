import os.path
import random
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from config import Config


class DesktopPet(QWidget):
    name = "DesktopPet"

    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        self.index = 0
        self.cfg = Config()

        self.is_follow_mouse = False
        self.mouse_drag_pos = self.pos()

        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()
        self.resize(128, 128)
        self.pet_images, icon_path = self.load_images()

        image = QImage()
        self.image = QLabel(self)
        self.set_image(self.pet_images[0][0])

        self.show()

        # 宠物动画动作执行所需的一些变量
        self.is_running_action = False
        self.action_images = []
        self.action_pointer = 0
        self.action_max_len = 0
        # 每隔一段时间做个动作
        self.timer_act = QTimer()
        self.timer_act.timeout.connect(self.random_act)
        self.timer_act.start(500)

    def set_image(self, image):
        self.image.setPixmap(QPixmap.fromImage(image))

    def load_image(self, image_path):
        image = QImage()
        image.load(image_path)
        return image

    def load_images(self):
        pet_images = []
        actions = self.cfg.PET_ACTIONS_MAP["fox"]
        for action in actions:
            pet_images.append(
                [self.load_image(os.path.join(self.cfg.ROOT_DIR, "fox", 'shime' + item + '.png')) for item in action])
        iconpath = os.path.join(self.cfg.ROOT_DIR, "fox", 'shime1.png')
        return pet_images, iconpath

    '''随机做一个动作'''
    def random_act(self):
        if not self.is_running_action:
            self.is_running_action = True
            self.action_images = random.choice(self.pet_images)
            self.action_max_len = len(self.action_images)
            self.action_pointer = 0
        self.run_frame()

    '''完成动作的每一帧'''
    def run_frame(self):
        if self.action_pointer == self.action_max_len:
            self.is_running_action = False
            self.action_pointer = 0
            self.action_max_len = 0
        self.set_image(self.action_images[self.action_pointer])
        self.action_pointer += 1

    '''鼠标左键按下时, 宠物将和鼠标位置绑定'''
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    '''鼠标移动, 则宠物也移动'''
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()
    '''鼠标释放时, 取消绑定'''
    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    pet.show()

    sys.exit(app.exec_())
