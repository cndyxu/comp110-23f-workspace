"""File to define River class."""

__author__ = "730479883"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """A river simulation of fish and bears."""
    def __init__(self, num_fish: int, num_bears: int):  
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]
        # for x in range(0, num_fish):
        #     self.fish.append(Fish())
        # for x in range(0, num_bears):
        #     self.bears.append(Bear())

    def check_ages(self):
        """Checks ages and removes any Fish."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Removes frontmost fish from river."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        """Bear eats 3 fish if there are 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Removes bears with hunger scores less than zero."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        
    def repopulate_fish(self):
        """Adds more fish to ecosystem."""
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(new_fish)])
    
    def repopulate_bears(self):
        """Adds more bears to ecosystem."""
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])
    
    def view_river(self):
        """Allows to simulate the river on any day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()
            self.view_river()
