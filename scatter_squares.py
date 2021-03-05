import matplotlib.pyplot as plt

plt.style.use('seaborn')
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s =10)
# Set the crath title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis='both', which='major', labelsize = 14)
ax.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
