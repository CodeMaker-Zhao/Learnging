from random import randint
import pygal

class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')