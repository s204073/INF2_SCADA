
class SteamTurbine:
    def __init__(self,reactor):
        self.reactor = reactor
        self.energy = 0
        self.generated_mega_watts()

    def generated_mega_watts(self):
        sum_of_control_rods = (self.reactor.control_rod_1 + self.reactor.control_rod_2 + self.reactor.control_rod_3 + self.reactor.control_rod_4)

        self.energy = (1000*sum_of_control_rods)/370
