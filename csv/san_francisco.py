import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/san_francisco_2020.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"No data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

fig, ax = plt.subplots()
plt.style.use('seaborn')
plt.title("High and low temperature comparison for San Francisco -2020", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.1)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()

