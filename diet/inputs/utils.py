#- Header -----------------------------------------------------------------
from scitools.StringFunction import StringFunction
import numpy as np
from models import Pulse_Inst

#--------------------------------------------------------------------------
def createplot1d(Food_Inst):
	    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	    from matplotlib.figure import Figure
	    from matplotlib.dates import DateFormatter
	    fig = Figure(edgecolor='white',facecolor='white')
	    ax  = fig.add_subplot(111)
	    x = np.linspace(float(plot1d.startpoint),\
	                    float(plot1d.endpoint),\
	                    float(plot1d.steps))
	    function = StringFunction(plot1d.function)
	    y = []
	    for i in range(len(x)):
	        y = np.append(y,function(x[i]))
	    ax.plot(x,y)
	    ax.set_xlabel('x')
	    ax.set_ylabel('y = f(x)')
	    canvas = FigureCanvas(fig)
	    return canvas

def textplot1d(Food_Inst):
	    x = np.linspace(float(plot1d.startpoint),\
	                    float(plot1d.endpoint),\
	                    float(plot1d.steps))
	    function = StringFunction(plot1d.function)
	    y = []
	    for i in range(len(x)):
	        y = np.append(y,function(x[i]))
	    return x,y
