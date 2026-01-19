from reactor import Reactor
from condenser import Condenser


class Pipe:
    def __init__(self,reactor):
        self.reactor = reactor
        self.condenser = Condenser(reactor)
        self.water = self.condenser.water

        
