"""Testing the River class with simulations."""

from exercises.ex08.river import River

my_river = River(num_fish=10, num_bears=2)
my_river.view_river()

r = River(5, 10)
r.one_river_week()