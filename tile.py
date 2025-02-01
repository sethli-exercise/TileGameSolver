class Tile:
    def __init__(self, state: bool = False):
        self.state = state

    def switchState(self):
        self.state = not self.state