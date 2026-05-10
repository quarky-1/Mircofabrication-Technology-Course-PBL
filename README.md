# ThinFilmLab: Virtual Simulator for Thin Film Deposition

![Python](https://img.shields.io/badge/Python-3.13-blue)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)
![NumPy](https://img.shields.io/badge/Numerical-NumPy-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

An interactive virtual laboratory simulator for understanding and visualizing thin film deposition processes used in semiconductor fabrication and microfabrication technology.

This project was developed as part of the **Micro Fabrication Technology PBL** under the Department of Electronics and Communication Engineering at **Jaypee Institute of Information Technology (JIIT), Noida**.

---

# 📘 About the Project

Thin film deposition is one of the most fundamental processes in semiconductor fabrication, MEMS manufacturing, nanotechnology, and materials engineering.

This project provides a simplified but educational simulation environment where users can:

- Select different thin film deposition techniques
- Change fabrication parameters interactively
- Observe deposition rate variations
- Visualize thickness growth over time
- Understand process behavior intuitively

The simulator models three major deposition techniques:

- Thermal Evaporation
- Sputtering
- Chemical Vapor Deposition (CVD)

The system combines:
- Mathematical process modeling
- Interactive PyQt6 GUI
- Real-time graph visualization using Matplotlib

---

# 🚀 Features

## ✅ Interactive GUI
- Built using **PyQt6**
- Easy-to-use simulation interface
- Real-time parameter control

## ✅ Multiple Deposition Techniques
Supports:
- Thermal Evaporation
- Sputtering
- Chemical Vapor Deposition (CVD)

## ✅ Adjustable Parameters
Users can modify:
- Temperature (K)
- Pressure
- Material Type
- Target Thickness (nm)

## ✅ Material Selection
Available materials:
- Aluminum
- Copper
- Silicon
- SiO₂

## ✅ Real-Time Simulation
- Calculates deposition rate
- Computes required deposition time
- Displays simulation results instantly

## ✅ Graph Visualization
- Thickness vs Time graph
- Dynamic Matplotlib plotting
- Real-time visualization updates

## ✅ Reset Functionality
Quickly restore default parameters for repeated experimentation.

---

# 🧠 Mathematical Models Used

## 1️⃣ Thermal Evaporation

The deposition rate is modeled as:

```math
Rate \propto \frac{T}{P}
```

Where:
- T = Temperature
- P = Pressure

Higher temperature increases deposition rate, while higher pressure reduces it.

---

## 2️⃣ Sputtering

Modeled using:

```math
Rate = k \cdot T \cdot (P + 1)
```

Where:
- k = scaling constant
- T = Temperature
- P = Pressure

This simulates plasma-assisted deposition behavior.

---

## 3️⃣ Chemical Vapor Deposition (CVD)

Implemented using Arrhenius behavior:

```math
Rate = e^{-E_a/(kT)}
```

Where:
- \(E_a\) = Activation energy
- \(k\) = Boltzmann constant
- \(T\) = Temperature

This demonstrates the strong temperature dependence of CVD processes.

---

# 📊 Simulation Output

The simulator provides:

- Deposition Rate
- Required Time
- Thickness Growth Curve

The graph visualizes:

```math
Thickness = Rate \times Time
```

---

# 🖥️ GUI Overview

The interface contains:

- Deposition Method Selector
- Material Selector
- Temperature Slider
- Pressure Slider
- Thickness Slider
- Run Simulation Button
- Reset Button
- Real-Time Graph Panel

---

# 🏗️ Project Architecture

```text
ThinFilmLab/
│
├── models/
│   ├── evaporation.py
│   ├── sputtering.py
│   └── cvd.py
│
├── ui/
│   └── main_window.py
│
├── visualization/
│   └── graph.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| PyQt6 | GUI Development |
| NumPy | Numerical Computation |
| Matplotlib | Graph Visualization |

---

# 📦 Dependencies

Main dependencies used:

- PyQt6
- NumPy
- Matplotlib

Full dependency list available in:

```text
requirements.txt
```

---

# 🔧 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/quarky-1/Mircofabrication-Technology-Course-PBL.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Mircofabrication-Technology-Course-PBL
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python main.py
```

---

# 📈 Observed Results

## Thermal Evaporation
- Higher temperature → Higher deposition rate
- Higher pressure → Lower deposition rate
- Linear thickness growth observed

## Sputtering
- Rate increases with temperature and pressure
- Stable linear growth achieved

## CVD
- Strong exponential dependence on temperature
- High sensitivity to parameter variation

---

# 🎯 Educational Significance

This simulator is useful for:

- Semiconductor fabrication learning
- Microfabrication education
- Virtual laboratory demonstrations
- Thin film deposition visualization
- Process parameter analysis
- Engineering coursework and projects

---

# 🔮 Future Scope

Possible future enhancements:

- More accurate physical models
- 2D/3D visualization
- Multi-layer deposition simulation
- Time-dependent rate variation
- Data export support
- Advanced semiconductor process integration

---

# 👨‍💻 Authors

- Sarthak Tripathi
- Charitra Chauhan
- Nav Arora

Department of Electronics and Communication Engineering  
Jaypee Institute of Information Technology, Noida

---

# 📄 Documentation

The complete project report includes:
- Methodology
- Mathematical models
- Simulation analysis
- Experimental observations
- Results and conclusions

---

# 📚 References

- Semiconductor Fabrication Fundamentals
- Thin Film Deposition Principles
- PyQt6 Documentation
- Matplotlib Documentation
- NumPy Documentation

---

# ⭐ Acknowledgement

We sincerely thank:

**Dr. Shradha Saxena**  
Department of Electronics and Communication Engineering  
JIIT Noida

for guidance and support throughout the project.

---

# 📌 Repository

GitHub Repository:

https://github.com/quarky-1/Mircofabrication-Technology-Course-PBL
