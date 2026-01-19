from steam_turbine import SteamTurbine


class Reactor:
    def __init__(self):
        self.control_rod_1 = 0
        self.control_rod_2 = 0
        self.control_rod_3 = 0
        self.control_rod_4 = 0

        self.water_level = 100
        self.power = 0
        self.state_of_work = False
        self.explosion = False
        self.steam_level = 0


        self.steam_turbine = None
        self.reactor_update_state()

    def set_rod_1(self, value):
        print(f"rod_1 {value}")
        self.control_rod_1 = value
        self.reactor_update_state()

    def set_rod_2(self, value):
        self.control_rod_2 = value
        self.reactor_update_state()

    def set_rod_3(self, value):
        self.control_rod_3 = value
        self.reactor_update_state()

    def set_rod_4(self, value):
        self.control_rod_4 = value
        self.reactor_update_state()




    def generated_power(self):
        sum_of_control_rods = self.control_rod_1 + self.control_rod_2 + self.control_rod_3 + self.control_rod_4
        if 49 < sum_of_control_rods <= 70:
            self.power = 1
        elif 70 < sum_of_control_rods <= 150:
            self.power = 2
        elif 150 < sum_of_control_rods <= 250:
            self.power = 3
        elif 250 < sum_of_control_rods <= 375:
            self.power = 4
        elif sum_of_control_rods > 390:
            self.power = 5
        else:
            self.power = 0

    def is_it_working(self):
        if self.power > 0 and self.power < 5:
            self.state_of_work = True
        elif self.power == 5:
            self.explosion = True
            self.state_of_work = False
        else:
            self.state_of_work = False

    def reactor_feedback(self):
        print("reactor feedback\n")
        print(f"control rods: {self.control_rod_1}, {self.control_rod_2}, {self.control_rod_3}, {self.control_rod_4}") #fstring
        print("power: ", self.power)
        print("state: ", self.state_of_work)
        print("explosion: ",self.explosion)


    def generated_steam(self):
        self.steam_level = self.power


    def reactor_update_state(self):
        self.generated_power()
        self.generated_steam()
        self.is_it_working()
        self.reactor_feedback()
        if self.steam_turbine is None:
            self.steam_turbine = SteamTurbine(self)
        else:
            self.steam_turbine.generated_mega_watts()



