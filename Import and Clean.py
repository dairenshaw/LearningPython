# Import packages
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

# Load the Parkrun csv data
data = pd.read_csv("ParkrunData.csv")
data['Date'] = pd.to_datetime(data['Date'])
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.time

# Select my runs only
dai = data.loc[data['Parkrunner'] == 'David RENSHAW']

# Register plot converters
register_matplotlib_converters()

# Plot
plt.plot(dai['Date'], dai['Time'], 'bo')
plt.title("My Parkrun Progress")
plt.xlabel("Date")
plt.ylabel("Time")
plt.show()
