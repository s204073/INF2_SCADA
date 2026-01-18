from PyQt5 import QtWidgets
from ui_control_panel import UiControlPanel

class ControlPanel(QtWidgets.QWidget, UiControlPanel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)      #layout odziedziczopny po ui

        #podlaczanie sygnalow
        #slidery
        