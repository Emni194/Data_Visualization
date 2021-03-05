from plotly.graph_objs import scatter, Layout
import numpy as np
import plotly.express as px

from random_walk import RandomWalk

while True:
    rw = RandomWalk(500_000)
    rw.fill_walk()

    point_numbers= range(rw.num_points)
    df = px.data.iris()
    color = np.random.randn(500),  # set color equal to a variable
    colorscale = 'Viridis',  # one of plotly colorscales
    fig = px.scatter(rw.x_values, rw.y_values, point_numbers)
    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break


