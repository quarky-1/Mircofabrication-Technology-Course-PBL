from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QComboBox, QSlider
)
from PyQt6.QtCore import Qt
import numpy as np

from models.evaporation import evaporation_rate
from models.sputtering import sputtering_rate
from models.cvd import cvd_rate
from visualization.graph import GraphCanvas


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thin Film Deposition Simulator")

        layout = QVBoxLayout()

        # ------------------ METHOD ------------------
        layout.addWidget(QLabel("Select Method"))
        self.method = QComboBox()
        self.method.addItems(["Thermal Evaporation", "Sputtering", "CVD"])
        layout.addWidget(self.method)

        # ------------------ MATERIAL ------------------
        layout.addWidget(QLabel("Material"))
        self.material = QComboBox()
        self.material.addItems(["Aluminum", "Copper", "Silicon", "SiO2"])
        layout.addWidget(self.material)

        # ------------------ TEMPERATURE ------------------
        layout.addWidget(QLabel("Temperature (K)"))

        self.temp_slider = QSlider(Qt.Orientation.Horizontal)
        self.temp_slider.setRange(300, 1200)
        self.temp_slider.setValue(300)

        self.temp_value = QLabel("300 K")
        self.temp_slider.valueChanged.connect(
            lambda v: self.temp_value.setText(f"{v} K")
        )

        layout.addWidget(self.temp_slider)
        layout.addWidget(self.temp_value)

        # ------------------ PRESSURE ------------------
        layout.addWidget(QLabel("Pressure"))

        self.pressure_slider = QSlider(Qt.Orientation.Horizontal)
        self.pressure_slider.setRange(1, 100)
        self.pressure_slider.setValue(1)

        self.pressure_value = QLabel("1")
        self.pressure_slider.valueChanged.connect(
            lambda v: self.pressure_value.setText(f"{v}")
        )

        layout.addWidget(self.pressure_slider)
        layout.addWidget(self.pressure_value)

        # ------------------ TARGET THICKNESS ------------------
        layout.addWidget(QLabel("Target Thickness (nm)"))

        self.thickness_slider = QSlider(Qt.Orientation.Horizontal)
        self.thickness_slider.setRange(10, 1000)
        self.thickness_slider.setValue(100)

        self.thickness_value = QLabel("100 nm")
        self.thickness_slider.valueChanged.connect(
            lambda v: self.thickness_value.setText(f"{v} nm")
        )

        layout.addWidget(self.thickness_slider)
        layout.addWidget(self.thickness_value)

        # ------------------ BUTTON ------------------
        self.button = QPushButton("Run Simulation")
        self.button.clicked.connect(self.run_simulation)
        layout.addWidget(self.button)

        # ------------------ RESET BUTTON ------------------
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_values)
        layout.addWidget(self.reset_btn)

        # ------------------ OUTPUT ------------------
        self.result = QLabel("Output will appear here")
        layout.addWidget(self.result)

        # ------------------ GRAPH ------------------
        self.graph = GraphCanvas()
        layout.addWidget(self.graph)

        self.setLayout(layout)

    # ------------------ SIMULATION FUNCTION ------------------
    def run_simulation(self):
        T = self.temp_slider.value()
        P = self.pressure_slider.value()
        target_thickness = self.thickness_slider.value()
        method = self.method.currentText()
        material = self.material.currentText()

        # Base rate
        if method == "Thermal Evaporation":
            rate = evaporation_rate(T, P)
        elif method == "Sputtering":
            rate = sputtering_rate(T, P)
        else:
            rate = cvd_rate(T)

        # Material scaling factor
        material_factor = {
            "Aluminum": 1.0,
            "Copper": 0.8,
            "Silicon": 0.6,
            "SiO2": 0.5
        }

        rate *= material_factor[material]

        # Time calculation
        if rate > 0:
            time_required = target_thickness / rate
        else:
            time_required = 0

        # Graph data
        time = np.linspace(0, time_required, 100)
        thickness = rate * time

        # Output
        self.result.setText(
            f"Material: {material}\n"
            f"Deposition Rate: {rate:.4f} nm/s\n"
            f"Time Required: {time_required:.2f} s"
        )

        self.graph.plot(time, thickness)

    # ------------------ RESET FUNCTION ------------------
    def reset_values(self):
        self.temp_slider.setValue(300)
        self.pressure_slider.setValue(1)
        self.thickness_slider.setValue(100)
        self.material.setCurrentIndex(0)

        self.result.setText("Output will appear here")
        self.graph.ax.clear()
        self.graph.draw()