from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6 and D10
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list
results = [die_1.roll() + die_2.roll() for num in range(1000)]


# Analyze the results.
max_result = die_2.num_sides + die_1.num_sides
frequencies = [results.count(value) for value in range (2, max_result+1)]

# Visualize the results
x_values = list(range(1, max_result+ 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='results of rolling three D6 1000000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
