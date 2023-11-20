"""File to define Fish class."""


class Fish:
    """A fish in a river ecosystem."""
    def __init__(self):
        """Init for class Fish."""
        self.age = 0
    
    def one_day(self):
        """Increase the age each day."""
        self.age += 1
        