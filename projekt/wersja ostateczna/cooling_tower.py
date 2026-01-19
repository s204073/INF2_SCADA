from condenser import Condenser
from steam_turbine import SteamTurbine



class CoolingTower:
    def __init__(self,reactor):
        self.reactor = reactor
        self.condenser = Condenser(reactor)
        self.steam_turbine = SteamTurbine(reactor)
        self.heat = 20
        self.update_heat()

    def update_heat(self):
        self.heat += self.steam_turbine.energy
        if self.heat > 1020:
            print("Too Hot!")

    def cooling(self, valve_1):
        if valve_1 == True:
            cooling_amount = min(1000, self.heat - 20)
            self.heat -= cooling_amount
            if self.heat <= 20:
                print("Safe temperature was restored")
            else:
                print("Valved is closed, theres no cooling!")
