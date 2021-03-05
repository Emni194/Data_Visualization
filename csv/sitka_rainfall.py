import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, precipiations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precipiation = float(row[3])
        precipiations.append(precipiation)
        dates.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipiations)
plt.title("Rain", fontsize=36)
plt.xlabel('', fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()
plt.show()




