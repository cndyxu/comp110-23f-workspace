"""File to define Bear class."""


class Bear:
    """A bear in a river ecosystem."""
    def __init__(self):
        """Init for class Bear."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Increases age every day and decreses hunger score each day."""
        self.age += 1
        self.hunger_score -= 1
    
    def eat(self, num_fish):
        """Correlated hunger score with number of fish."""
        self.hunger_score += num_fish
    