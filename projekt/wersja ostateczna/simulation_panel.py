from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtGui import QPen, QBrush, QColor, QPainterPath
from PyQt5.QtCore import Qt, QPoint, QPointF, QTimer, QPropertyAnimation, QEasingCurve

#===================KLASY OBIEKTOW==============================

class DReactorTank(QGraphicsRectItem):
    def __init__(self, parent_scene, x=100, y=100, w=110, h=400):
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
        colors = {0: QColor(154,225,252), 30: QColor(182, 201, 36), 80: QColor(201, 122, 36), 100: QColor(201, 64, 36)}
        self.level_of_water.setBrush(QBrush(colors.get(water_level // 25 * 25, QColor(0, 150, 255))))


class DReactor1ControlRod(QGraphicsRectItem):
    def __init__(self, scene, x_pos):
        super().__init__(x_pos, 200, 10, 120)
        self.setBrush(QBrush(QColor(60, 60, 60)))
        self.setPen(QPen(QColor(40, 40, 40)))
        scene.addItem(self)
        self.home_x = float(x_pos)
        self.home_y = 80

    def update_position(self, position):
        y_offset = (100-position*1.2)
        self.setPos(self.home_x,self.home_y+y_offset)


# class DReactor4ControlRods:
#     def __init__(self, parent_scene):
#         self.rods = []
#         x_positions = [120, 140, 160, 180]
#         for x in x_positions:
#             rod = DReactor1ControlRod(x, parent_scene)
#             self.rods.append(rod)
#
#     def update_positions(self, rods_values):
#         for i, rod in enumerate(self.rods):
#             rod.set_position(rods_values[i])
#
#

class DNeutronsBox(QGraphicsRectItem):
    def __init__(self, parent_scene, x=115, y=375, w=80, h=125):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)

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
    def __init__(self, parent_scene, x=600, y=250, w=100, h=100):
        super().__init__(x, y, w, h)
        self.setBrush(QBrush(QColor(150, 150, 150)))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)


class Pipe1:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(223, 120))
        self.path.lineTo(QPoint(336, 120))
        self.pipe1 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 25))

class Pipe2:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(400, 360))
        self.path.lineTo(QPoint(400, 475))
        self.path.lineTo(QPoint(223, 475))

        self.pipe2 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 25))

class Pipe3:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(462, 120))
        self.path.lineTo(QPoint(536, 120))
        self.pipe3 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 25))

class Pipe4:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(400, 160))
        self.path.lineTo(QPoint(400, 235))
        self.pipe4 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 25))

class Pipe5:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(595, 270))
        self.path.lineTo(QPoint(430, 270))
        self.path.lineTo(QPoint(430, 320))
        self.path.lineTo(QPoint(595, 320))
        self.pipe5 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 15))

class FuelRod1:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(125, 385))
        self.path.lineTo(QPoint(125, 495))
        self.fuelrod1 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 5))

class FuelRod2:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(145, 385))
        self.path.lineTo(QPoint(145, 495))
        self.fuelrod2 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 5))

class FuelRod3:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(165, 385))
        self.path.lineTo(QPoint(165, 495))
        self.fuelrod3 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 5))

class FuelRod4:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(185, 385))
        self.path.lineTo(QPoint(185, 495))
        self.fuelrod4 = self.scene.addPath(self.path, QPen(QColor(67, 153, 250), 5))

class SteamPath:
    def __init__(self, scene):
        self.scene = scene
        self.path = QPainterPath()
        self.path.moveTo(QPoint(223, 120))
        self.path.lineTo(QPoint(336, 120))
        self.path.lineTo(QPoint(400, 160))
        self.path.lineTo(QPoint(400, 235))
        self.steam_path = self.scene.addPath(self.path, QPen(QColor('white'), 4))


class DValve1(QGraphicsRectItem):  # DValve1!
    def __init__(self, parent_scene, x=400, y=700, w=30, h=50, valve_state=False):
        super().__init__(x, y, w, h)
        color = QColor(255, 255, 255) if valve_state else QColor(0, 0, 0)
        self.setBrush(QBrush(color))
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.parent_scene = parent_scene
        parent_scene.addItem(self)
        self.valve_open = valve_state

    def update_state(self, open):
        self.valve_open = open
        color = QColor(255, 255, 255) if open else QColor(0, 0, 0)
        self.setBrush(QBrush(color))

#=====================KLASY ANIMACJI============================

class FlowAnimation:
    def __init__(self, scene, pipe_path, flow_type='steam'):
        self.scene = scene
        self.pipe_path = pipe_path
        self.flow_type = flow_type
        self.color = QColor(255, 255, 100, 150) if flow_type == 'steam' else QColor(0, 150, 255, 180)
        self.thickness = 12

        self.flow_item = scene.addPath(pipe_path, QPen(self.color, self.thickness))
        self.offset = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_flow)

    def animate_flow(self):
        self.offset = (self.offset + 5) % 100
        alpha = int(50 + 150 * (self.offset / 100))
        self.flow_item.setPen(
            QPen(QColor(self.color.red(), self.color.green(), self.color.blue(), alpha), self.thickness))

    def set_active(self, active):
        if active:
            self.timer.start(100)
        else:
            self.timer.stop()


class DWaterLevel(QGraphicsRectItem):
    def __init__(self, tank_parent):
        super().__init__(0, 0, 0, 0)
        self.tank = tank_parent
        self.setParentItem(tank_parent)
        self.setBrush(QBrush(QColor(0, 150, 255, 200)))
        self.setPen(QPen(Qt.NoPen))

    def update_level(self, level_percent):  # 0-100
        h = (level_percent / 100.0) * self.tank.rect().height() * 0.8
        self.setRect(5, self.tank.rect().height() - h - 5,
                     self.tank.rect().width() - 10, h)

        # Kolor wg poziomu (zagrożenie)
        if level_percent > 90:
            self.setBrush(QColor(255, 50, 50, 200))  # czerwony
        elif level_percent > 70:
            self.setBrush(QColor(255, 150, 0, 200))  # pomarańcz
        else:
            self.setBrush(QColor(0, 150, 255, 200))  # niebieski


class SimulationPanel:
    def __init__(self,scene, parent=None):
        self.scene = scene
        self.control_rods = []
        self.reactor_tank = DReactorTank(self.scene)
        self.reactor_water = DWaterLevel(self.reactor_tank)

        self.neutrony = DNeutronsBox(self.scene)
        # Narysuj wszystko
        x_positions = [60, 70, 80, 90]
        for x in x_positions:
            rod = DReactor1ControlRod(self.scene, x)
            self.control_rods.append(rod)
        self.update_positions([0, 0, 0, 0])

        # self.control_rods = DReactor4ControlRods(self.scene)
        self.steam_turbine = DSteamTurbineTank(self.scene)
        self.generator = DGeneratorTank(self.scene)
        self.condenser = DCondenserTank(self.scene)
        self.condenser_water = DWaterLevel(self.condenser)
        self.cooling_tower = DCoolingTowerTank(self.scene)

        self.pipe1 = Pipe1(self.scene)
        self.pipe2 = Pipe2(self.scene)
        self.pipe3 = Pipe3(self.scene)
        self.pipe4 = Pipe4(self.scene)
        self.pipe5 = Pipe5(self.scene)
        self.fuelrod1 = FuelRod1(self.scene)
        self.fuelrod2 = FuelRod2(self.scene)
        self.fuelrod3 = FuelRod3(self.scene)
        self.fuelrod4 = FuelRod4(self.scene)

        self.valve1_display = DValve1(self.scene, 400, 700, 30, 50, False)







        # Animacje przepływu w rurach
        self.steam_path = SteamPath(self.scene)
        self.steam_flow = FlowAnimation(self.scene, self.steam_path.path, 'steam')
        self.water_flow = FlowAnimation(self.scene, self.pipe2.path, 'water')

    def update_flows(self, reactor_power, condenser_water, valve_1):
        self.steam_flow.set_active(reactor_power > 0)
        self.water_flow.set_active(valve_1)
        self.reactor_water.update_level(reactor.water_level)
        self.condenser_water.update_level(condenser_water / 4)

    def update_valves(self, valve_1):
        self.valve1_display.update_state(valve_1)

    def update_positions(self, positions):
        for i, pos in enumerate(positions):
            self.control_rods[i].update_position(pos)