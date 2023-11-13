class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        self.age += 1

    def eat(self, fish):
        self.hunger_score = 0
        return fish
    
