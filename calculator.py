#!/usr/bin/env python3

testAtoms = [
    [1, 100, 10, 10],
    [1, 200, 20, 20],
    [2, 300, 30, 30],
    [3, 400, 40, 40]]

from math import sin, cos, radians

from options import options

class calculator():

    def __init__(self, alpha=0, beta=0, gamma=0):
        self.update(alpha, beta, gamma)

    def update(self, alpha, beta, gamma):
        self.alpha = radians(alpha) 
        self.beta = radians(beta)
        self.gamma = radians(gamma)
        self.calculateMatrix()
        self.threeMatrices()
        self.moveAtoms()
        self.computeRotatedAtomsCoords()

    def calculateMatrix(self):
        al = self.alpha
        be = self.beta
        ga = self.gamma
        a11 = cos(al) * cos(ga) - sin(al) * cos(be) * sin(ga)
        a12 = -cos(al) * sin(ga) - sin(al) * cos(be) * cos(ga)
        a13 = sin(al) * sin(be)
        a21 = sin(al) * cos(ga) + cos(al) * cos(be) * sin(ga)
        a22 = -sin(al) * sin(ga) + cos(al) * cos(be) * cos(ga)
        a23 = -cos(al) * sin(be)
        a31 = sin(be) * sin(ga)
        a32 = sin(be) * cos(ga)
        a33 = cos(be)
        self.rotationMatrix = [[a11, a12, a13], 
                               [a21, a22, a23],
                               [a31, a32, a33]]

    def threeMatrices(self):
        a11 = 1
        a12 = a13 = a21 = a31 = 0
        a22 = a33 = cos(self.alpha)
        a32 = sin(self.alpha)
        a23 = -sin(self.alpha)
        mx = [[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]]
        a11 = a33 = cos(self.beta)
        a13 = sin(self.beta)
        a31 = -sin(self.beta)
        a21 = a12 = a32 = a23 = 0
        a22 = 1
        my = [[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]]
        a33 = 1
        a31 = a32 = a23 = a13 = 0
        a22 = a11 = cos(self.gamma)
        a21 = sin(self.gamma)
        a12 = -sin(self.gamma)
        mz = [[a11, a12, a13],
              [a21, a22, a23],
              [a31, a32, a33]]

        a11 = mx[0][0] * my[0][0] + mx[0][1] * my[1][0] + mx[0][2] * my[2][0]
        a12 = mx[0][0] * my[0][1] + mx[0][1] * my[1][1] + mx[0][2] * my[2][1]
        a13 = mx[0][0] * my[0][2] + mx[0][1] * my[1][2] + mx[0][2] * my[2][2]
        a21 = mx[1][0] * my[0][0] + mx[1][1] * my[1][0] + mx[1][2] * my[2][0]
        a22 = mx[1][0] * my[0][1] + mx[1][1] * my[1][1] + mx[1][2] * my[2][1]
        a23 = mx[1][0] * my[0][2] + mx[1][1] * my[1][2] + mx[1][2] * my[2][2]
        a31 = mx[2][0] * my[0][0] + mx[2][1] * my[1][0] + mx[2][2] * my[2][0]
        a32 = mx[2][0] * my[0][1] + mx[2][1] * my[1][1] + mx[2][2] * my[2][1]
        a33 = mx[2][0] * my[0][2] + mx[2][1] * my[1][2] + mx[2][2] * my[2][2]

        mxmy = [[a11, a12, a13], 
                [a21, a22, a23],
                [a31, a32, a33]]

        a11 = mxmy[0][0] * mz[0][0] + mxmy[0][1] * mz[1][0] + mxmy[0][2] * mz[2][0]
        a12 = mxmy[0][0] * mz[0][1] + mxmy[0][1] * mz[1][1] + mxmy[0][2] * mz[2][1]
        a13 = mxmy[0][0] * mz[0][2] + mxmy[0][1] * mz[1][2] + mxmy[0][2] * mz[2][2]
        a21 = mxmy[1][0] * mz[0][0] + mxmy[1][1] * mz[1][0] + mxmy[1][2] * mz[2][0]
        a22 = mxmy[1][0] * mz[0][1] + mxmy[1][1] * mz[1][1] + mxmy[1][2] * mz[2][1]
        a23 = mxmy[1][0] * mz[0][2] + mxmy[1][1] * mz[1][2] + mxmy[1][2] * mz[2][2]
        a31 = mxmy[2][0] * mz[0][0] + mxmy[2][1] * mz[1][0] + mxmy[2][2] * mz[2][0]
        a32 = mxmy[2][0] * mz[0][1] + mxmy[2][1] * mz[1][1] + mxmy[2][2] * mz[2][1]
        a33 = mxmy[2][0] * mz[0][2] + mxmy[2][1] * mz[1][2] + mxmy[2][2] * mz[2][2]

        mxmymz = [[a11, a12, a13],
                  [a21, a22, a23],
                  [a31, a32, a33]]

        self.rotXYZMatrice = mxmymz


    def moveAtoms(self):
        movedAtoms = []
        x = y = z = 0
        for atom in testAtoms:
            x += atom[1]
            y += atom[2]
            x += atom[3]
        x /= len(testAtoms)
        y /= len(testAtoms)
        z /= len(testAtoms)
        for atom in testAtoms:
            movedAtoms.append([atom[0], atom[1] - x, atom[2] - y, atom[3] - z])
        self.movedAtoms = movedAtoms

    def computeRotatedAtomsCoords(self):
        self.calculateMatrix()
        #m = self.rotationMatrix
        m = self.rotXYZMatrice
        newAtoms = []
        for atom in self.movedAtoms:
            x = atom[1] * m[0][0] + atom[2] * m[0][1] + atom[3] * m[0][2]
            y = atom[1] * m[1][0] + atom[2] * m[1][1] + atom[3] * m[1][2]
            z = atom[1] * m[2][0] + atom[2] * m[2][1] + atom[3] * m[2][2]
            newAtoms.append([atom[0], x, y, x])
        self.atomsToDraw = newAtoms
        
    def getAtomsToDraw(self):
        return self.atomsToDraw

    def getRotationMatrix(self):
        return self.rotationMatrix

    def getRotXYZMatrice(self):
        return self.rotXYZMatrice
