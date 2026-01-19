#window_nuclear_pp.py - power plant
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtCore import QSize


from Control_panel_widget import ControlPanel
from cooling_tower import CoolingTower
from reactor import Reactor
from simulation_panel import SimulationPanel
from steam_turbine import SteamTurbine


class NuclearPowerPlantWindow(QMainWindow):
    def __init__(self):
        super(NuclearPowerPlantWindow, self).__init__()
        self.setMinimumSize(QSize(1200, 800))
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
        self.control_panel.setMaximumWidth(350)
        self.control_panel.setMinimumWidth(280)

        self.control_panel_widget = ControlPanel()
        cp_layout.addWidget(self.control_panel_widget)


        secondary_layout = QHBoxLayout()
        secondary_layout.addWidget(self.cp_tittle)
        secondary_layout.addWidget(self.control_panel)
        secondary_layout.addStretch(1)



        #simulation panel
        self.simulation_panel = QWidget(self)
        sim_layout = QVBoxLayout(self.simulation_panel)

        self.sim_tittle = QLabel("Simulation Panel")
        sim_layout.addWidget(self.sim_tittle)

        #twqrzenie sceny
        self.scene = QGraphicsScene(0,0,800, 600)

        #widok scena
        self.graphics_view = QGraphicsView(self.scene)

        #zeby nie wywalalo
        self.graphics_view.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        self.graphics_view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        self.graphics_view.setMaximumWidth(800)
        self.graphics_view.setMinimumWidth(600)
        self.graphics_view.setSceneRect(0,0,800,600)
        sim_layout.addWidget(self.graphics_view)

        self.simulation_graphics = SimulationPanel(self.scene)

        #simpanel ze scena
        self.simulation_panel.setMinimumWidth(600)
        secondary_layout.addWidget(self.simulation_panel)
        overriding_layout.addLayout(secondary_layout)


        #podlaczanie sygnalow
        self.reactor = Reactor()


        self.control_panel_widget.rod_1_changed.connect(self.reactor.set_rod_1)
        self.control_panel_widget.rod_2_changed.connect(self.reactor.set_rod_2)
        self.control_panel_widget.rod_3_changed.connect(self.reactor.set_rod_3)
        self.control_panel_widget.rod_4_changed.connect(self.reactor.set_rod_4)

        self.control_panel_widget.valve_1_changed.connect(self.reactor.switch_valve_1)
        self.control_panel_widget.valve_2_changed.connect(self.reactor.switch_valve_2)

        #update grafiki
        self.control_panel_widget.rod_1_changed.connect(self.update_graphics_all)
        self.control_panel_widget.rod_2_changed.connect(self.update_graphics_all)
        self.control_panel_widget.rod_3_changed.connect(self.update_graphics_all)
        self.control_panel_widget.rod_4_changed.connect(self.update_graphics_all)
        self.control_panel_widget.valve_1_changed.connect(self.update_graphics_all)
        self.control_panel_widget.valve_2_changed.connect(self.update_graphics_all)
        # self.control_panel_widget.rod_1_changed.connect(self.update_graphics_rods)
        # self.control_panel_widget.rod_2_changed.connect(self.update_graphics_rods)
        # self.control_panel_widget.rod_3_changed.connect(self.update_graphics_rods)
        # self.control_panel_widget.rod_4_changed.connect(self.update_graphics_rods)


    def update_graphics_rods(self):
        self.simulation_graphics.update_positions([
            self.reactor.control_rod_1,
            self.reactor.control_rod_2,
            self.reactor.control_rod_3,
            self.reactor.control_rod_4])

    def update_graphics_all(self):
        self.update_graphics_rods()
        self.simulation_graphics.steam_flow.set_active(self.reactor.power > 0)
        self.simulation_graphics.water_flow.set_active(self.reactor.valve_1)












