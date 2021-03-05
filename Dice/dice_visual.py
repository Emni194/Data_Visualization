from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6 and D10
die_1 = Die()
die_2 = Die(10)
# Make some rolls and store results in a list
results = []
for roll in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_2.num_sides + die_1.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result+ 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='results of rolling two D6 and D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks, as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(500_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolors='none', s = 1)

    # Emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break