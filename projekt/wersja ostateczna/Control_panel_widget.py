from PyQt5 import QtWidgets, QtCore
from ui_control_panel import UiControlPanel
from PyQt5.QtCore import pyqtSignal

class ControlPanel(QtWidgets.QWidget, UiControlPanel):
        #podlaczanie sygnalow
        #skladnia = widget[self.slider1,self.valve1].signal[clicked/stateChanged/valueChanged].connect(funkcja[def on_event()])
        #slidery
    rod_1_changed = QtCore.pyqtSignal(int)
    rod_2_changed = QtCore.pyqtSignal(int)
    rod_3_changed = QtCore.pyqtSignal(int)
    rod_4_changed = QtCore.pyqtSignal(int)

    valve_1_changed = QtCore.pyqtSignal(bool)
    # valve_2_changed = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  #laduje layout z ui

        self.slider_1.valueChanged.connect(self.slider_1_changed)       #slider_1_changed - jako pomost -funkcja przetwarzajaca wartosc z slidera
        self.slider_2.valueChanged.connect(self.slider_2_changed)
        self.slider_3.valueChanged.connect(self.slider_3_changed)
        self.slider_4.valueChanged.connect(self.slider_4_changed)

        self.valve_1.toggled.connect(self.valve_1_switched)
        # self.valve_2.toggled.connect(self.valve_2_switched)


    def slider_1_changed(self, value):
        self.rod_1_changed.emit(value)

    def slider_2_changed(self, value):
        self.rod_2_changed.emit(value)

    def slider_3_changed(self, value):
        self.rod_3_changed.emit(value)

    def slider_4_changed(self, value):
        self.rod_4_changed.emit(value)


    def valve_1_switched(self, checked):
        self.valve_1_changed.emit(checked)

    # def valve_2_switched(self, checked):
    #     self.valve_2_changed.emit(checked)


    #wplyw innych czynnikow na rody
    def set_control_rods(self, rod_1, rod_2, rod_3, rod_4):
        self.slider_1.setValue(rod_1)
        self.slider_2.setValue(rod_2)
        self.slider_3.setValue(rod_3)
        self.slider_4.setValue(rod_4)

    def set_valves(self, valve_1):
        self.valve_1.setChecked(valve_1)
        # self.valve_2.setChecked(valve_2)