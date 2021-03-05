import csv
from datetime import datetime

from matplotlib import pyplot as plt

def get_weather_data(filename, dates, precips, date_index, precips_index):
    """Get the highs and lows from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                precip = float(row[precips_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                precips.append(precip)


# Get weather data for Sitka.
filename = 'data/sitka_weather_2018_simple.csv'
dates, precips = [], []
get_weather_data(filename, dates, precips, date_index=2, precips_index=3)

# Plot Sitka weather data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='red')

# Get weather data for Death Valley.
filename = 'data/death_valley_2018_simple.csv'
dates, precips = [], []
get_weather_data(filename, dates, precips, date_index=2, precips_index=3)


# Add Death Valley data to current plot.
ax.plot(dates, precips, c='blue')

# Format plot.
title = "Daily Rainfall- 2018"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()