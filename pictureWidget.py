#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from options import options
from calculator import calculator

class pictureWidget(QWidget):

    def __init__(self, o, alpha=0, beta=0, gamma=0):
        super().__init__()
        self.setFixedSize(o.screenSize, o.screenSize)
        self.beginX = self.beginY = self.endX = self.endY = 0
        self.o = o
        self.c = calculator()
        self.atomsToDraw = self.c.getAtomsToDraw()
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)

    def changeAngles(self, alpha, beta, gamma):
        self.c.update(alpha, beta, gamma)
        self.atomsToDraw = self.c.getAtomsToDraw()
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.update()

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            self.beginX = event.pos().x()
            self.beginY = event.pos().y()
        if event.type() == QEvent.MouseMove and event.buttons() == Qt.LeftButton:
            self.endX = event.pos().x()
            self.endY = event.pos().y()
            if self.endX - self.beginX !=0:
                self.changeAngles(self.alpha + (self.endX - self.beginX) / 1000,
                                  self.beta + (self.endX - self.beginX) / 1000, self.gamma)
                self.beginX = (self.endX - self.beginX) / 0.99
                self.beginY = (self.endY - self.beginY) / 0.99
            #if self.beginX != self.endX:
            #    self.beginX = self.endX
            #if self.beginY != self.endY:
            #    self.beginY = self.endY
            #self.update()
        return QWidget.eventFilter(self, source, event)

    def paintEvent(self, event):
        axisPainter = QPainter()
        axisPainter.begin(self)
        axisPainter.setBrush(QBrush(QColor(50, 50, 50)))
        m = self.c.getRotXYZMatrice()
        axisPainter.drawLine(250, 250, 
                            (m[0][0] + 1) * 250, 
                            (m[1][0] + 1) * 250)
        axisPainter.drawText((0.9*m[0][0] + 1) * 250, (0.9*m[1][0] + 1) * 250, 'X')
        axisPainter.drawLine(250, 250, 
                            (m[0][1] + 1) * 250,
                            (m[1][1] + 1) * 250)
        axisPainter.drawText((0.9*m[0][1] + 1) * 250, (0.9*m[1][1] + 1) * 250, 'Y')
        axisPainter.drawLine(250, 250, 
                            (m[0][2] + 1) * 250,
                            (m[1][2] + 1) * 250)
        axisPainter.drawText((0.9*m[0][2] + 1) * 250, (0.9*m[1][2] + 1) * 250, 'Z')
        axisPainter.end()

        p = QPainter()
        p.begin(self)
        p.setBrush(QBrush(QColor(0, 255, 0)))
        for atom in self.atomsToDraw:
            p.drawEllipse(atom[1] + self.width() / 2, 
                          atom[2] + self.width() / 2, 10, 10)
        p.end()
