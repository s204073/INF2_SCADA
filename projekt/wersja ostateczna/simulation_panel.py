from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt


class DReactorTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=110, y=100, w=100, h=200):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)
        self.level_of_water = None

    def set_water_level(self, water_level):  # 0-100
        if self.level_of_water:
            self.parent_scene.removeItem(self.level_of_water)
        h = (water_level / 100.0) * 150
        self.level_of_water = QGraphicsRectItem(
            self.x() + 5,
            self.rect().y() + self.rect().height() - h,
            self.rect().width() - 10, h
        )
        self.level_of_water.setBrush(QBrush(QColor(0, 150, 255)))
        self.level_of_water.setParentItem(self)
        # Kolory wg poziomu
        colors = {0: QColor(5, 116, 161), 30: QColor(182, 201, 36), 80: QColor(201, 122, 36), 100: QColor(201, 64, 36)}
        self.level_of_water.setBrush(QBrush(colors.get(water_level // 25 * 25, QColor(0, 150, 255))))


class DReactor1ControlRod(QGraphicsRectItem):
    def __init__(self, x, parent_scene, max_h=200):
        super().__init__(x, 100, 10, 0)
        self.x = x
        self.max_h = max_h
        self.setBrush(QBrush(QColor(60, 60, 60)))
        self.setPen(QPen(QColor(40, 40, 40)))
        parent_scene.addItem(self)

    def set_position(self, position):
        h = (position / 100.0) * self.max_h
        self.setRect(self.x, 300 - h, 15, h)


class DReactor4ControlRods:
    def __init__(self, parent_scene):
        self.rods = []
        x_positions = [120, 140, 160, 180]
        for x in x_positions:
            rod = DReactor1ControlRod(x, parent_scene)
            self.rods.append(rod)

    def update_positions(self, rods_values):
        for i, rod in enumerate(self.rods):
            rod.set_position(rods_values[i])





class DSteamTurbineTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=350, y=100, w=100, h=50):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)


class DGeneratorTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=550, y=100, w=100, h=50):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)

class DCondenserTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=350, y=250, w=100, h=100):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)


class DCoolingTowerTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=650, y=250, w=100, h=100):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)



class SimulationPanel:
    def __init__(self,scene, parent=None):
        self.scene = scene

        # Narysuj wszystko
        self.reactor_tank = DReactorTank(self.scene)
        self.control_rods = DReactor4ControlRods(self.scene)
        self.steam_turbine = DSteamTurbineTank(self.scene)
        self.generator = DGeneratorTank(self.scene)
        self.condenser = DCondenserTank(self.scene)
        self.cooling_tower = DCoolingTowerTank(self.scene)

