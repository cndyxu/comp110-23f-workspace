from fish import Fish
from bear import Bear

class River:
    def __init__(self, num_fish, num_bears):
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]
        self.day = 0
    
    def view_river(self):
        num_fish = len(self.fish)
        num_bears = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bears}")

    def one_river_day(self):
        for fish in self.fish:
            fish.one_day()

        for bear in self.bears:
            bear.one_day()

        self.day += 1

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()
        
    def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
    
    def fish_population(self):
        return len(self.fish)
    
    def bear_population(self):
        return len(self.bears)
