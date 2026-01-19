class Condenser:    #skraplacz
    def __init__(self,reactor):
        self.reactor = reactor
        self.water = 0
        self.condensed_water()

    def condensed_water(self):
        sum_of_control_rods = (self.reactor.control_rod_1 + self.reactor.control_rod_2 + self.reactor.control_rod_3 + self.reactor.control_rod_4)

        self.water = sum_of_control_rods
