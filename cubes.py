import matplotlib.pyplot as plt

plt.style.use('seaborn')
x_values=range(1, 5000)
y_values=[x**3 for x in x_values]
fg, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.set_title('Cubes')
ax.set_xlabel('Value')
ax.set_ylabel('Cube Value')
ax.axis([0, 5000, 0, 125000000000])
plt.show()

