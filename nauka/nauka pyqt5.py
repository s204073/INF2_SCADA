#---------------zadanie 1 ---podstawy, okno
# from PyQt5.QtWidgets import QApplication, QMainWindow   #QApplication (app handler), QWidget to klasy
# import sys      #dostep do wiersza polecen
#
# #jedna aplikacja na jedna aplikacje, sys.argv - pozwala czytac linie kodu, nie jest niezbedne jak command line nie uzywany, wtedy ([])
# app = QApplication(sys.argv)
#
# window = QMainWindow()                #nasze okno
# window.show()                       #defaultowo okna sa schowane
#
# app.exec()                          #start the event loop

#=----------------------zadanie2--- nazwa rozamiry przycisk
# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
# #sublcass Qmainwindow to customize your aplication's main window, using def__init__(self)
# class MainWindow(QMainWindow):
#     def __init__(self):         #superclass is always called __init__
#         super().__init__()
#
#         self.setWindowTitle("Moja wspaniala aplikacja")
#         button = QPushButton("Press me!")
#
#         self.setMinimumSize(QSize(300, 200))    #min rozmiar
#         self.setMaximumSize(QSize(600, 400))    #max rozmiar
#         #self.setFixedSize(QSize(400,300))   #rozmair zablokowany okna
#
#         #ustaw widgert przycisku na srodku
#         self.setCentralWidget(button)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

#------------------------zadanie 3  --- orzelaxcznie przycisku w rozne stany
#there are two methods: signals&slots, events
#signal is being received by slots, which can be any fucntion or method
# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Moja wspaniala aplikacja")
#         self.setFixedSize(QSize(400, 300))
#
#         button = QPushButton("Spusc bombe")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)     #przelaczony
#
#         self.setCentralWidget(button)
#
# # moze byc wcisniety albo nie, to sprawdza true false czy wcisniety, czyli przelacznik, np swiatla
#     def the_button_was_clicked(self):
#         print("Click")
#
#     def the_button_was_toggled(self, checked):
#         print("checked?", checked)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


#---------------zadanie 4 - przypisywanie zmiennej do stanu
# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.button_is_checked = True
#
#         self.setWindowTitle("Moja wspaniala aplikacja")
#         self.setFixedSize(QSize(400, 300))
#
#         button = QPushButton("Spusc bombe")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_toggled)     #przelaczony
#         button.setChecked(self.button_is_checked)
#
#         self.setCentralWidget(button)
#
#     def the_button_was_toggled(self, checked):
#         self.button_is_checked = checked
#         print(self.button_is_checked)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
#

#-------------zadanie 5---- output w oknie, nie w konsoli
# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Moja wspaniala aplikacja")
#         self.setFixedSize(QSize(400, 300))
#
#         self.button = QPushButton("Spusc bombe")
#         self.button.clicked.connect(self.the_button_was_clicked)
#
#         self.setCentralWidget(self.button)
#
#     def the_button_was_clicked(self):
#         self.button.setText("Spuscilem sie juz")
#         self.button.setEnabled(False)       #To disable a button call .setEnabled() with False
#
#         self.setWindowTitle("zuzyta aplikacja")
#         self.setFixedSize(QSize(100, 30))
#
# #Again, because we need to be able to access the button in our the_button_was_clicked method,
# # we keep a reference to it on self.
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

#


# #----------------------zadanie 7-- wypluwanie tekstu do labelu immediately
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
# import sys
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("ciekawe co aplikacja tym razem wypluje")
#         self.setFixedSize(500, 200)
#
#         self.label = QLabel()
#         self.input = QLineEdit()
#         self.input.textChanged.connect(self.label.setText)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.input)
#         layout.addWidget(self.label)
#
#         container = QWidget()
#         container.setLayout(layout)
#
#         self.setCentralWidget(container)
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec_()


# #-----------------zadanei 8 - eventy
# #event- kazda interacja uzytkownika z aplikacja
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setMouseTracking(True)
#         self.label = QLabel("Prosze nacisnac w tym oto oknie bo inaczej bede gryzl")
#         self.label.setMouseTracking(True)
#         self.setCentralWidget(self.label)
#         self.setFixedSize(400, 400)
#
#         #We need to use .setMouseTracking on both the label and window here,
#         # because the label completely covers the window and would otherwise
#         # block the events.
#
#     def mouseMoveEvent(self, e):
#         self.label.setText("nie uciekaj")
#
#     # def mousePressEvent(self, e):
#     #     self.label.setText("trzymasz, dobrze")
#     def mousePressEvent(self, e):
#         if e.button() == Qt.LeftButton:
#             # handle the left-button press in here
#             self.label.setText("mousePressEvent LEFT")
#
#         elif e.button() == Qt.MiddleButton:
#             # handle the middle-button press in here.
#             self.label.setText("mousePressEvent MIDDLE")
#
#         elif e.button() == Qt.RightButton:
#             # handle the right-button press in here.
#             self.label.setText("mousePressEvent RIGHT")
#
#     def mouseReleaseEvent(self, e):
#         self.label.setText("czemu pusciles?")
#
#     def mouseDoubleClickEvent(self, e):
#         self.label.setText("wow")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec_()


# #---------------zadanie 9 ------ events types
#
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.show()
#
#         self.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.customContextMenuRequested.connect(self.on_context_menu)
#
#     def on_context_menu(self, pos):
#         context = QMenu(self)
#         context.addAction(QAction("test 1", self))
#         context.addAction(QAction("test 2", self))
#         context.addAction(QAction("test 3", self))
#         context.exec(self.mapToGlobal(pos))
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


# #-------------zadanie 11- QLabel
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDoubleSpinBox,
#     QLabel,
#     QLineEdit,
#     QListWidget,
#     QMainWindow,
#     QSlider,
#     QSpinBox,
# )
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QLabel("Hello")
#         font = widget.font()
#         font.setPointSize(30)
#         widget.setFont(font)
#         widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#
#         self.setCentralWidget(widget)
#
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# #-----------zadanie 12 -- QCheckBox
#
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDoubleSpinBox,
#     QLabel,
#     QLineEdit,
#     QListWidget,
#     QMainWindow,
#     QSlider,
#     QSpinBox,
# )
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QCheckBox()
#         # widget.setCheckState(Qt.Checked)
#
#         widget.setCheckState(Qt.PartiallyChecked)
#         # Or: widget.setTriState(True)
#         widget.stateChanged.connect(self.show_state)
#
#         self.setCentralWidget(widget)
#
#     def show_state(self, s):
#         print(s == Qt.Checked)
#         print(s)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
#

# #--------------zadanei 13 - QComboBox
#
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDoubleSpinBox,
#     QLabel,
#     QLineEdit,
#     QListWidget,
#     QMainWindow,
#     QSlider,
#     QSpinBox,
# )
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QComboBox()
#         widget.addItems(["One", "Two", "Three"])
#
#         # Sends the current index (position) of the selected item.
#         widget.currentIndexChanged.connect( self.index_changed )
#
#         # There is an alternate signal to send the text.
#         widget.currentTextChanged.connect( self.text_changed )
#
#         self.setCentralWidget(widget)
#
#     def index_changed(self, i): # i is an int
#         print(i)
#
#     def text_changed(self, s): # s is a str
#         print(s)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


# #-------------zadanie 13---- QListWidget
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDoubleSpinBox,
#     QLabel,
#     QLineEdit,
#     QListWidget,
#     QMainWindow,
#     QSlider,
#     QSpinBox,
# )
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QListWidget()
#         widget.addItems(["One", "Two", "Three"])
#
#         widget.currentItemChanged.connect(self.index_changed)
#         widget.currentTextChanged.connect(self.text_changed)
#
#         self.setCentralWidget(widget)
#
#     def index_changed(self, i): # Not an index, i is a QListWidgetItem
#         print(i.text())
#
#     def text_changed(self, s): # s is a str
#         print(s)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


# #-----------zadaenie 14---- QLineEdit
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDoubleSpinBox,
#     QLabel,
#     QLineEdit,
#     QListWidget,
#     QMainWindow,
#     QSlider,
#     QSpinBox,
# )
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText("Enter your text")
#
#         #widget.setReadOnly(True) # uncomment this to make it read-only
#
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)
#
#         self.setCentralWidget(widget)
#
#     def return_pressed(self):
#         print("Return pressed!")
#         self.centralWidget().setText("BOOM!")
#
#     def selection_changed(self):
#         print("Selection changed")
#         print(self.centralWidget().selectedText())
#
#     def text_changed(self, s):
#         print("Text changed...")
#         print(s)
#
#     def text_edited(self, s):
#         print("Text edited...")
#         print(s)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# #-----------zadanei 15 - QSpinBox and QDoubleSpinBox
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox, QLabel, QLineEdit, QListWidget, QMainWindow, QSlider, QSpinBox,)
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QSpinBox()
#         # Or: widget = QDoubleSpinBox()
#
#         widget.setMinimum(-10)
#         widget.setMaximum(3)
#         # Or: widget.setRange(-10,3)
#
#         widget.setPrefix("$")
#         widget.setSuffix("c")
#         widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
#         widget.valueChanged.connect(self.value_changed)
#         widget.textChanged.connect(self.value_changed_str)
#
#         self.setCentralWidget(widget)
#
#     def value_changed(self, i):
#         print(i)
#
#     def value_changed_str(self, s):
#         print(s)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
#



# #-----------zadanei 16 - QSlider
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox, QLabel, QLineEdit, QListWidget, QMainWindow, QSlider, QSpinBox,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QSlider(Qt.Horizontal) #lub Qt.Vertical
#
#         widget.setMinimum(-10)
#         widget.setMaximum(3)
#         # Or: widget.setRange(-10,3)
#
#         widget.setSingleStep(3)
#
#         widget.valueChanged.connect(self.value_changed)
#         widget.sliderMoved.connect(self.slider_position)
#         widget.sliderPressed.connect(self.slider_pressed)
#         widget.sliderReleased.connect(self.slider_released)
#
#         self.setCentralWidget(widget)
#
#     def value_changed(self, i):
#         print(i)
#
#     def slider_position(self, p):
#         print("position", p)
#
#     def slider_pressed(self):
#         print("Pressed!")
#
#     def slider_released(self):
#         print("Released")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
#



# #-----------zadanei 17 - QDial, cos nie dziala mi
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (QApplication, QDial, QCheckBox, QComboBox, QDoubleSpinBox, QLabel, QLineEdit, QListWidget, QMainWindow, QSlider, QSpinBox,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QDial()
#         widget.setRange(-10, 100)
#         widget.setSingleStep(0.5)
#
#         widget.valueChanged.connect(self.value_changed)
#         widget.sliderMoved.connect(self.slider_position)
#         widget.sliderPressed.connect(self.slider_pressed)
#         widget.sliderReleased.connect(self.slider_released)
#
#         self.setCentralWidget(widget)
#
#     def value_changed(self, i):
#         print(i)
#
#     def slider_position(self, p):
#         print("position", p)
#
#     def slider_pressed(self):
#         print("Pressed!")
#
#     def slider_released(self):
#         print("Released")
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


# # #-----------zadanei 18 - QVBoxLayout
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
# from PyQt5.QtGui import QPalette, QColor
#
#
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QVBoxLayout()
#
#         layout.addWidget(Color('red'))
#         layout.addWidget(Color('green'))
#         layout.addWidget(Color('blue'))
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

# # #-----------zadanei 19 - QHBoxLayout
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
# from PyQt5.QtGui import QPalette, QColor
#
#
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QHBoxLayout()
#
#         layout.addWidget(Color('red'))
#         layout.addWidget(Color('green'))
#         layout.addWidget(Color('blue'))
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()



# # #-----------zadanei 20 - Nesting Layout
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QVBoxLayout
# from PyQt5.QtGui import QPalette, QColor
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout1 = QHBoxLayout()
#         layout2 = QVBoxLayout()
#         layout3 = QVBoxLayout()
#
#         layout1.setContentsMargins(0,0,0,0)
#         layout1.setSpacing(10)
#
#         layout2.addWidget(Color('red'))
#         layout2.addWidget(Color('yellow'))
#         layout2.addWidget(Color('purple'))
#
#         layout1.addLayout( layout2 )
#
#         layout1.addWidget(Color('green'))
#
#         layout3.addWidget(Color('red'))
#         layout3.addWidget(Color('purple'))
#
#         layout1.addLayout( layout3 )
#
#         widget = QWidget()
#         widget.setLayout(layout1)
#         self.setCentralWidget(widget)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

# # #-----------zadanei 21 - QGrid
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QVBoxLayout
# from PyQt5.QtGui import QPalette, QColor
#
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QGridLayout()
#
#         layout.addWidget(Color('red'), 0, 0)
#         layout.addWidget(Color('green'), 3, 5)
#         layout.addWidget(Color('blue'), 1, 1)
#         layout.addWidget(Color('purple'), 2, 1)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


# #----------zadanie 22 - QStacked (ciekawostak)
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )
# from PyQt5.QtGui import QPalette, QColor
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         pagelayout = QVBoxLayout()
#         button_layout = QHBoxLayout()
#         self.stacklayout = QStackedLayout()
#
#         pagelayout.addLayout(button_layout)
#         pagelayout.addLayout(self.stacklayout)
#
#         btn = QPushButton("red")
#         btn.pressed.connect(self.activate_tab_1)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("red"))
#
#         btn = QPushButton("green")
#         btn.pressed.connect(self.activate_tab_2)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("green"))
#
#         btn = QPushButton("yellow")
#         btn.pressed.connect(self.activate_tab_3)
#         button_layout.addWidget(btn)
#         self.stacklayout.addWidget(Color("yellow"))
#
#         widget = QWidget()
#         widget.setLayout(pagelayout)
#         self.setCentralWidget(widget)
#
#     def activate_tab_1(self):
#         self.stacklayout.setCurrentIndex(0)
#
#     def activate_tab_2(self):
#         self.stacklayout.setCurrentIndex(1)
#
#     def activate_tab_3(self):
#         self.stacklayout.setCurrentIndex(2)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


##----------zadanie 23 - QTabWidget (ciekawostak)
# import sys
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
#     QTabWidget
# )
# from PyQt5.QtGui import QPalette, QColor
#
# class Color(QWidget):
#     def __init__(self, color):
#         super().__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         tabs = QTabWidget()
#         tabs.setTabPosition(QTabWidget.West)
#         tabs.setMovable(True)
#
#         for n, color in enumerate(["red", "green", "blue", "yellow"]):
#             tabs.addTab(Color(color), color)
#
#         self.setCentralWidget(tabs)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

#
# #------------zadanie 24 --- toolbars
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QIcon, QKeySequence
# from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox,QLabel,QMainWindow,QStatusBar,QToolBar,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#
#         label = QLabel("Hello!")
#         label.setAlignment(Qt.AlignCenter)
#
#         self.setCentralWidget(label)
#
#         toolbar = QToolBar("My main toolbar")
#         toolbar.setIconSize(QSize(16,16))
#         self.addToolBar(toolbar)
#
#         button_action = QAction(QIcon("bug.png"), "Your button", self)
#         button_action.setStatusTip("This is your button")
#         button_action.triggered.connect(self.toolbar_button_clicked)
#         button_action.setCheckable(True)
#         toolbar.addAction(button_action)
#
#         self.setStatusBar(QStatusBar(self))
#
#     def toolbar_button_clicked(self, s):
#         print("click", s)
#
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# #------------zadanie 26 --- dwa guziki
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QIcon, QKeySequence
# from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox,QLabel,QMainWindow,QStatusBar,QToolBar,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#
#         label = QLabel("Hello!")
#         label.setAlignment(Qt.AlignCenter)
#
#         self.setCentralWidget(label)
#
#         toolbar = QToolBar("My main toolbar")
#         toolbar.setIconSize(QSize(16, 16))
#         self.addToolBar(toolbar)
#
#         button_action = QAction(QIcon("bug.png"), "&Your button", self)
#         button_action.setStatusTip("This is your button")
#         button_action.triggered.connect(self.toolbar_button_clicked)
#         button_action.setCheckable(True)
#         toolbar.addAction(button_action)
#
#         toolbar.addSeparator()
#
#         button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
#         button_action2.setStatusTip("This is your button2")
#         button_action2.triggered.connect(self.toolbar_button_clicked)
#         button_action2.setCheckable(True)
#         toolbar.addAction(button_action2)
#
#         toolbar.addWidget(QLabel("Hello"))
#         toolbar.addWidget(QCheckBox())
#
#         self.setStatusBar(QStatusBar(self))
#
#     def toolbar_button_clicked(self, s):
#         print("click", s)
#
#
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()

#
# #------------zadanie 27 --- menu
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QIcon, QKeySequence
# from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox,QLabel,QMainWindow,QStatusBar,QToolBar,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#
#         label = QLabel("Hello!")
#         label.setAlignment(Qt.AlignCenter)
#
#         self.setCentralWidget(label)
#
#         toolbar = QToolBar("My main toolbar")
#         toolbar.setIconSize(QSize(16, 16))
#         self.addToolBar(toolbar)
#
#         button_action = QAction(QIcon("bug.png"), "&Your button", self)
#         button_action.setStatusTip("This is your button")
#         button_action.triggered.connect(self.toolbar_button_clicked)
#         button_action.setCheckable(True)
#         toolbar.addAction(button_action)
#
#         toolbar.addSeparator()
#
#         button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
#         button_action2.setStatusTip("This is your button2")
#         button_action2.triggered.connect(self.toolbar_button_clicked)
#         button_action2.setCheckable(True)
#         toolbar.addAction(button_action2)
#
#         toolbar.addWidget(QLabel("Hello"))
#         toolbar.addWidget(QCheckBox())
#
#         self.setStatusBar(QStatusBar(self))
#
#         menu = self.menuBar()
#
#         file_menu = menu.addMenu("&File")
#         file_menu.addAction(button_action)
#         file_menu.addSeparator()
#
#         file_submenu = file_menu.addMenu("Submenu")
#         file_submenu.addAction(button_action2)
#
#     def toolbar_button_clicked(self, s):
#         print("click", s)
#
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()

# #------------zadanie 28 --- keyboard shortcuts
# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QIcon, QKeySequence
# from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox,QLabel,QMainWindow,QStatusBar,QToolBar,)
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#
#         label = QLabel("Hello!")
#
#         # The `Qt` namespace has a lot of attributes to customize
#         # widgets. See: http://doc.qt.io/qt-5/qt.html
#         label.setAlignment(Qt.AlignCenter)
#
#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(label)
#
#         toolbar = QToolBar("My main toolbar")
#         toolbar.setIconSize(QSize(16, 16))
#         self.addToolBar(toolbar)
#
#         button_action = QAction(QIcon("bug.png"), "&Your button", self)
#         button_action.setStatusTip("This is your button")
#         button_action.triggered.connect(self.toolbar_button_clicked)
#         button_action.setCheckable(True)
#         # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
#         # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
#         # or system agnostic identifiers (e.g. QKeySequence.Print)
#         button_action.setShortcut(QKeySequence("Ctrl+p"))
#         toolbar.addAction(button_action)
#
#         toolbar.addSeparator()
#
#         button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
#         button_action2.setStatusTip("This is your button2")
#         button_action2.triggered.connect(self.toolbar_button_clicked)
#         button_action2.setCheckable(True)
#         toolbar.addAction(button_action2)
#
#         toolbar.addWidget(QLabel("Hello"))
#         toolbar.addWidget(QCheckBox())
#
#         self.setStatusBar(QStatusBar(self))
#
#         menu = self.menuBar()
#
#         file_menu = menu.addMenu("&File")
#         file_menu.addAction(button_action)
#
#         file_menu.addSeparator()
#
#         file_submenu = file_menu.addMenu("Submenu")
#
#         file_submenu.addAction(button_action2)
#
#     def toolbar_button_clicked(self, s):
#         print("click", s)
#
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()

#
# # #DIALOGS AND ALERTS
# #------------zadanie 29 ----------
# import sys
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
#
#
#     def button_clicked(self, s):
#         print("click", s)
#
#         dlg = CustomDialog()
#         if dlg.exec():
#             print("Success!")
#         else:
#             print("Cancel!")
#
#         dlg = QDialog(self)
#         dlg.setWindowTitle("HELLO!")
#         dlg.exec()
#
# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.setWindowTitle("HELLO!")
#
#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
#
#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)
#
#         layout = QVBoxLayout()
#         message = QLabel("Something happened, is that OK?")
#         layout.addWidget(message)
#         layout.addWidget(self.buttonBox)
#         self.setLayout(layout)
#
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# #-----------------zadanie 30 - QMessageBox
# import sys
#
# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
#
#     # def button_clicked(self, s):
#     #     dlg = QMessageBox(self)
#     #     dlg.setWindowTitle("I have a question!")
#     #     dlg.setText("This is a question dialog")
#     #     dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#     #     dlg.setIcon(QMessageBox.Warning)        #tu sie daje ikone
#     #     button = dlg.exec()
#     #
#     #     if button == QMessageBox.Yes:
#     #         print("Yes!")
#     #     else:
#     #         print("No!")
#
#     # def button_clicked(self, s):
#     #     dlg = QMessageBox(self)
#     #     dlg.setWindowTitle("I have a question!")
#     #     dlg.setText("This is a simple dialog")
#     #     button = dlg.exec()
#     #
#     #     if button == QMessageBox.Ok:
#     #         print("OK!")
#
#     def button_clicked(self, s):
#         button = QMessageBox.critical(
#             self,
#             "Oh dear!",
#             "Something went very wrong.",
#             buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
#             defaultButton=QMessageBox.Discard,
#         )
#
#         if button == QMessageBox.Discard:
#             print("Discard!")
#         elif button == QMessageBox.NoToAll:
#             print("No to all!")
#         else:
#             print("Ignore!")
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


# #----------zadanie 31 -- nowe okna
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
#
# import sys
#
# from random import randint
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.w = None  # No external window yet.
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)
#
#     def show_new_window(self, checked):
#         if self.w is None:
#             self.w = AnotherWindow()
#             self.w.show()
#
#         else:
#             self.w.close()  # Close window.
#             self.w = None  # Discard reference.
#
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()


#---------zadanie 32 -- okno, co jest persistent
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
#
# import sys
#
# from random import randint
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.w = AnotherWindow()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.toggle_window)
#         self.setCentralWidget(self.button)
#
#     def toggle_window(self, checked):
#         if self.w.isVisible():
#             self.w.hide()
#
#         else:
#             self.w.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
#
# import sys
#
# from random import randint
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0,100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.w = AnotherWindow()
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.toggle_window)
#         self.setCentralWidget(self.button)
#
#     def toggle_window(self, checked):
#         if self.w.isVisible():
#             self.w.hide()
#
#         else:
#             self.w.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()


# #----------zadanie 33 - wiele okiien
# import sys
# from random import randint
#
# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """
#
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()
#
#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(self.toggle_window1)
#         l.addWidget(button1)
#
#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(self.toggle_window2)
#         l.addWidget(button2)
#
#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)
#
#     def toggle_window1(self, checked):
#         if self.window1.isVisible():
#             self.window1.hide()
#
#         else:
#             self.window1.show()
#
#     def toggle_window2(self, checked):
#         if self.window2.isVisible():
#             self.window2.hide()
#
#         else:
#             self.window2.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()

# #------------zadanie 34 - transmitting extra data with Qt signals
#
# import sys
# from random import randint
#
# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """
#
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()
#
#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(
#             lambda checked: self.toggle_window(self.window1)
#         )
#         l.addWidget(button1)
#
#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(
#             lambda checked: self.toggle_window(self.window2)
#         )
#         l.addWidget(button2)
#
#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)
#
#     def toggle_window(self, window):
#         if window.isVisible():
#             window.hide()
#
#         else:
#             window.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()


#===================RYSOWANIE LINII=========================
# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QGraphicsView,
#     QGraphicsScene,
#     QGraphicsEllipseItem,
# )
# from PyQt5.QtGui import QPainterPath, QTransform, QPen, QBrush, QColor, QPainter
# from PyQt5.QtCore import Qt
#
#
# PORT_PEN_COLOR = "#000000"
# PORT_BRUSH_COLOR = "#ebebeb"
# EDGE_PEN_COLOR = "#474747"
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(0, 0, 800, 600)
#         self.setCentralWidget(GraphicsView())
#         self.show()
#
#
# class GraphicsView(QGraphicsView):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setMouseTracking(True)
#         self.setScene(GraphicsScene())
#         self.setRenderHint(QPainter.RenderHint.Antialiasing)
#
#
# class GraphicsScene(QGraphicsScene):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setSceneRect(-10000, -10000, 20000, 20000)
#         self._port_pen = QPen(QColor(PORT_PEN_COLOR))
#         self._port_brush = QBrush(QColor(PORT_BRUSH_COLOR))
#         self._edge_pen = QPen(QColor(EDGE_PEN_COLOR))
#         self._edge_pen.setWidth(4)
#
#     def mousePressEvent(self, event):
#         clicked_item = self.itemAt(event.scenePos(), QTransform())
#         if event.buttons() == Qt.MouseButton.LeftButton:
#             if clicked_item is not None:
#                 # edge item
#                 pos = clicked_item.scenePos()
#                 pos.setX(pos.x() + 6)
#                 pos.setY(pos.y() + 6)
#                 self.edge = self.addPath(QPainterPath())
#                 self.edge.setPen(self._edge_pen)
#                 self.start_pos = pos
#                 self.end_pos = self.start_pos
#                 self.update_path()
#             else:
#                 x = event.scenePos().x()
#                 y = event.scenePos().y()
#                 # port item
#                 start_port = Ellipse()
#                 start_port.setPos(x - 6, y - 6)
#                 start_port.setPen(self._port_pen)
#                 start_port.setBrush(self._port_brush)
#                 start_port.setZValue(10000.0)
#                 self.addItem(start_port)
#                 # edge item
#                 self.edge = self.addPath(QPainterPath())
#                 self.edge.setPen(self._edge_pen)
#                 self.start_pos = event.scenePos()
#                 self.end_pos = self.start_pos
#                 self.update_path()
#
#     def mouseMoveEvent(self, event):
#         if event.buttons() == Qt.MouseButton.LeftButton:
#             print(f"moving, x : {event.scenePos().x()}, y : {event.scenePos().y()}")
#             self.end_pos = event.scenePos()
#             try:
#                 self.update_path()
#             except AttributeError:
#                 pass
#
#     def mouseReleaseEvent(self, event) -> None:
#         released_item = self.itemAt(event.scenePos(), QTransform())
#         if event.button() == Qt.MouseButton.LeftButton:
#             if released_item is not None and released_item.type() != 2:
#                 self.end_pos = released_item.scenePos()
#                 self.end_pos.setX(self.end_pos.x() + 6)
#                 self.end_pos.setY(self.end_pos.y() + 6)
#                 if not self.start_pos.isNull() and not self.end_pos.isNull():
#                     path = QPainterPath()
#                     path.moveTo(self.start_pos.x() - 1, self.start_pos.y() - 1)
#                     path.lineTo(self.end_pos)
#                     self.edge.setPath(path)
#             else:
#                 x = event.scenePos().x() + 1
#                 y = event.scenePos().y() + 1
#                 end_port = QGraphicsEllipseItem(0, 0, 10, 10)
#                 end_port.setPos(x - 6, y - 6)
#                 end_port.setPen(self._port_pen)
#                 end_port.setBrush(self._port_brush)
#                 end_port.setZValue(10000.0)
#                 self.addItem(end_port)
#
#     def update_path(self):
#         if not self.start_pos.isNull() and not self.end_pos.isNull():
#             path = QPainterPath()
#             path.moveTo(self.start_pos.x() - 1, self.start_pos.y() - 1)
#             path.lineTo(self.end_pos)
#             self.edge.setPath(path)
#
#
# class Ellipse(QGraphicsEllipseItem):
#     def __init__(self):
#         super().__init__()
#         self.setRect(0, 0, 10, 10)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     sys.exit(app.exec())

#---------z chata
