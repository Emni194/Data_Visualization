import matplotlib.pyplot as plt
from die_roll import Die
import numpy as np

die_1 = Die()
die_2 = Die()


plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots()
results = []
for num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies=[]
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency=results.count(value)
    frequencies.append(frequency)

x_values=list(range(2, max_results+1))
y_values=list(frequencies)
ax.set_title("Roll dice", fontsize = 24)
ax.set_xlabel("Result", fontsize=16)
ax.set_ylabel("Frequency of result", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize = 14)
plt.xticks(np.arange(min(x_values), max(x_values)+1, 1.0))

plt.bar(x_values, y_values, color=['red', 'blue', 'purple', 'green', 'lavender'])
plt.show()


