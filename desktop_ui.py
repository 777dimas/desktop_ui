#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser, subprocess, sys, time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import QMovie, QPainter, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget, QMessageBox


class DesktopWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ebutoon = QPushButton(self)
        self.ebutoon.setIcon(QIcon("pictures/exit_pic.png"))
        self.ebutoon.setIconSize(QSize(50, 50))
        self.ebutoon.move(1860, 0)
        self.ebutoon.clicked.connect(QCoreApplication.instance().quit)

        self.showFullScreen()
        self.movie = QMovie("pictures/background.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def paintEvent(self, event):
        current_frame = self.movie.currentPixmap()
        frame_rect = current_frame.rect()
        frame_rect.moveCenter(self.rect().center())
        if frame_rect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frame_rect.left(), frame_rect.top(), current_frame)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = DesktopWindow()
    sys.exit(app.exec_())
