import sys
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
from matplotlib import animation
from model import *
import matplotlib.pyplot  as plt


def show_graph(vals:list):
    t=vals[0]
    x=vals[1]
    y=vals[2]
    plt.scatter(t,x,color='b',label='presa')
    plt.scatter(t,y,color='r',label='depredador')
    plt.xlabel('tiempo t')
    plt.ylabel('Población')
    plt.show()


    
