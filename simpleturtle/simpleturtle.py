#!/usr/bin/python

from graphics import *
import numpy as np
import math


class Turtle:
    """Turtle class: creates turtle instances with drawing capabilities"""

    def __init__(self, name):
        self.name = name
        self.aTriangle = Polygon(Point(100, 90), Point(95, 105), Point(105, 105))
        self.colour = "red"
        self.aTriangle.setFill(self.colour)
        self.aTriangle.draw(win)
        self.penStatus = 1

    def setColour(self, colour):
        """Set Turtle colour"""
        self.colour = colour
        self.aTriangle.setFill(self.colour)

    def moveForward(self, d):
        """Move Turtle forward of d pixels"""
        pointList = self.aTriangle.getPoints()
        pointsCC = np.array([[pointList[0].getX(), pointList[1].getX(), pointList[2].getX()],
                             [pointList[0].getY(), pointList[1].getY(), pointList[2].getY()]])
        centreCC = np.sum(pointsCC, axis=1)/3
        headCC = pointsCC[:, 0]
        T = [d * (headCC[0] - centreCC[0]) / 10, d * (headCC[1] - centreCC[1]) / 10]

        if self.penStatus:
            aLine = Line(Point(centreCC[0], centreCC[1]), Point(centreCC[0] + T[0], centreCC[1] + T[1]))
            aLine.setOutline(self.colour)
            aLine.draw(win)

        self.aTriangle.move(T[0], T[1])

    def rotateLeft(self, d):
        """Rotate Turtle anti-clockwise of d pixels"""
        pointList = self.aTriangle.getPoints()
        pointsCC = np.array([[pointList[0].getX(), pointList[1].getX(), pointList[2].getX()],
                             [pointList[0].getY(), pointList[1].getY(), pointList[2].getY()]])
        centreCC = np.sum(pointsCC, axis=1, keepdims=True)/3

        R = np.array([[np.cos(math.radians(-d)), -np.sin(math.radians(-d))],
                      [np.sin(math.radians(-d)), np.cos(math.radians(-d))]])
        pointsCC_rot = np.dot(R, pointsCC-centreCC) + centreCC

        self.aTriangle.undraw()
        self.aTriangle = Polygon(Point(pointsCC_rot[0, 0], pointsCC_rot[1, 0]),
                                 Point(pointsCC_rot[0, 1], pointsCC_rot[1, 1]),
                                 Point(pointsCC_rot[0, 2], pointsCC_rot[1, 2]))
        self.aTriangle.setFill(self.colour)
        self.aTriangle.draw(win)

    def rotateRight(self, d):
        """Rotate Turtle clockwise of d pixels"""
        pointList = self.aTriangle.getPoints()
        pointsCC = np.array([[pointList[0].getX(), pointList[1].getX(), pointList[2].getX()],
                             [pointList[0].getY(), pointList[1].getY(), pointList[2].getY()]])
        centreCC = np.sum(pointsCC, axis=1, keepdims=True)/3

        R = np.array([[np.cos(math.radians(d)), -np.sin(math.radians(d))],
                      [np.sin(math.radians(d)), np.cos(math.radians(d))]])
        pointsCC_rot = np.dot(R, pointsCC-centreCC) + centreCC

        self.aTriangle.undraw()
        self.aTriangle = Polygon(Point(pointsCC_rot[0, 0], pointsCC_rot[1, 0]),
                                 Point(pointsCC_rot[0, 1], pointsCC_rot[1, 1]),
                                 Point(pointsCC_rot[0, 2], pointsCC_rot[1, 2]))
        self.aTriangle.setFill(self.colour)
        self.aTriangle.draw(win)

    def setPenUp(self):
        """Disable Turtle's drawing capability"""
        self.penStatus = 0

    def setPenDown(self):
        """Enable Turtle's drawing capability"""
        self.penStatus = 1

win = GraphWin()
