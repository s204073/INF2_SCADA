from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.Qt import QSize
from color import Color
from window_nuclear_pp import NuclearPowerPlantWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.setMinimumSize(QSize(200, 400))
        self.window_npp = NuclearPowerPlantWindow() #sygnal

        self.choice_nuclear_pp = QPushButton("Nuclear Power Plant") #przycisk
        self.choice_nuclear_pp.setStyleSheet(
            "background-color: yellow; color: black;"
        )
        self.choice_nuclear_pp.clicked.connect(self.toggle_nuclear_pp)


        layout = QVBoxLayout()

        # layout.addWidget(Color('red'))
        layout.addWidget(self.choice_nuclear_pp)
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))



        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # button - another window
    def toggle_nuclear_pp(self):
        # if self.choice_nuclear_pp.isVisible():
        #     self.window_npp.hide()
        # else:
        self.window_npp.show()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()