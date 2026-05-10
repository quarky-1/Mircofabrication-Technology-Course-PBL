from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

    def plot(self, time, thickness):
        self.ax.clear()
        self.ax.plot(time, thickness)
        self.ax.set_title("Thickness vs Time")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Thickness (nm)")
        self.ax.grid(True)
        self.draw()