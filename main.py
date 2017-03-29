#!/usr/bin/env python3
# coding utf-8

import sys
import copy
import random

import pprint
pprint = pprint.PrettyPrinter(indent=1).pprint

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from alapWidget import alapWidget
from options import options
from mouseTracker import mouseTracker

def main(): # alap
    app = QApplication(sys.argv)

    o = options()

    w = alapWidget(o)
    #w = mouseTracker()
    w.show()
    #app.installEventFilter(w)

    sys.exit(app.exec_())


main()
