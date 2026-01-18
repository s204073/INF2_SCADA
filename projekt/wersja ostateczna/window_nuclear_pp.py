#window_nuclear_pp.py - power plant
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QSize

from Control_panel_widget import ControlPanel


class NuclearPowerPlantWindow(QMainWindow):
    def __init__(self):
        super(NuclearPowerPlantWindow, self).__init__()
        self.setFixedSize(QSize(1200, 800))
        self.setWindowTitle("Nuclear Power Plant")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        overriding_layout = QVBoxLayout(central_widget)
        self.tittle = QLabel("Theres real fun here")
        overriding_layout.addWidget(self.tittle)

        #placeholdery
        #control panel
        self.control_panel = QWidget(self)
        self.cp_tittle = QLabel("Control Panel")
        cp_layout = QVBoxLayout(self.control_panel)

        secondary_layout = QHBoxLayout()
        secondary_layout.addWidget(self.cp_tittle)
        secondary_layout.addWidget(self.control_panel)



        #simulation panel
        self.simulation_panel = QWidget(self)
        sim_layout = QVBoxLayout(self.simulation_panel)
        secondary_layout.addWidget(self.simulation_panel)


        self.sim_tittle = QLabel("Simulation Panel")
        secondary_layout.addWidget(self.sim_tittle)

        overriding_layout.addLayout(secondary_layout)

        self.control_panel_widget = ControlPanel()
        cp_layout.addWidget(self.control_panel_widget)






