import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, precips = [], []
    for row in reader:
        precip = float(row[3])
        precips.append(precip)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot( dates, precips)
plt.title("Rain in Dead Valley", fontsize = 12)
plt.xlabel("", fontsize = 12)
plt.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()
plt.show()