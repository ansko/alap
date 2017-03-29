#!/usr/bin/env python3
# coding utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from options import options
from pictureWidget import pictureWidget

class alapWidget(QWidget):

    o = options()

    def __init__(self, o):
        super().__init__()
        self.alpha = 0
        self.beta = 0
        self.gamma = 0
        self.setMouseTracking(True)
        self.makeWidget()

    def makeWidget(self, alpha=0, beta=0, gamma=0):
        self.sliderAlpha = QSlider(Qt.Horizontal)
        self.sliderAlpha.setMinimum(-1)
        self.sliderAlpha.setMaximum(91)
        self.sliderAlpha.setFixedSize(250, 30)
        self.sliderAlpha.setTickInterval(1)
        self.sliderAlpha.sliderMoved.connect(self.changeAlpha)

        self.textAlpha = QTextEdit()
        self.textAlpha.setFixedSize(50, 30)

        self.sliderBeta = QSlider(Qt.Horizontal)
        self.sliderBeta.setMinimum(-1)
        self.sliderBeta.setMaximum(91)
        self.sliderBeta.setFixedSize(250, 30)
        self.sliderBeta.setTickInterval(1)
        self.sliderBeta.sliderMoved.connect(self.changeBeta)

        self.textBeta = QTextEdit()
        self.textBeta.setFixedSize(50, 30)

        self.sliderGamma = QSlider(Qt.Horizontal)
        self.sliderGamma.setMinimum(-1)
        self.sliderGamma.setMaximum(91)
        self.sliderGamma.setFixedSize(250, 30)
        self.sliderGamma.setTickInterval(1)
        self.sliderGamma.sliderMoved.connect(self.changeGamma)

        self.textGamma = QTextEdit()
        self.textGamma.setFixedSize(50, 30)

        self.l = pictureWidget(self.o, alpha, beta, gamma)
        self.l.installEventFilter(self.l)
        self.l.setFixedSize(self.l.width(), self.l.height())

        v = QVBoxLayout()
        v.setSpacing(0)
        v.addWidget(self.sliderAlpha)
        v.addWidget(self.textAlpha)
        v.addWidget(self.sliderBeta)
        v.addWidget(self.textBeta)
        v.addWidget(self.sliderGamma)
        v.addWidget(self.textGamma)

        h = QHBoxLayout()
        h.setSpacing(0)
        h.addLayout(v)
        h.addWidget(self.l)
        self.setLayout(h)

    def changeAlpha(self):
        self.textAlpha.setText(str(self.sliderAlpha.value()))
        self.alpha = self.sliderAlpha.value()
        self.l.changeAngles(self.alpha, self.beta, self.gamma)
        self.update()

    def changeBeta(self):
        self.textBeta.setText(str(self.sliderBeta.value()))
        self.beta = self.sliderBeta.value()
        self.l.changeAngles(self.alpha, self.beta, self.gamma)
        self.update()

    def changeGamma(self):
        self.textGamma.setText(str(self.sliderGamma.value()))
        self.gamma = self.sliderGamma.value()
        self.l.changeAngles(self.alpha, self.beta, self.gamma)
        self.update()
