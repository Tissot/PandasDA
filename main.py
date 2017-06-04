import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import date, datetime, time
import time
import seaborn as sns

# Import San Francisco Bay Area Weather data from CSV file
data = pd.read_csv('weather.csv')

# Make variables some friendlier names for users
old_names = ['Max TemperatureF', 'Min TemperatureF', 'Mean TemperatureF', 'Max Dew PointF', 'MeanDew PointF',
             'Min DewpointF', 'Max Humidity',
             ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn', ' Mean Sea Level PressureIn',
             ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles',
             ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn',
             ' CloudCover', ' WindDirDegrees']
new_names = ['maxTemp', 'minTemp', 'meanTemp', 'maxDew', 'meanDew', 'minDew', 'maxHum', 'meanHum', 'minHum', 'maxPress',
             'minPress', 'meanPress', 'maxVis', 'meanVis',
             'minVis', 'maxWind', 'meanWind', 'maxGust', 'preIn', 'cloud', 'WindDir']
data.rename(columns=dict(zip(old_names, new_names)), inplace=True)


# Set Fahrenheit Scale to Celsius Scale F -> *C
"""
for column in data(['minTemp, meanTemp, maxTemp']):
    print(column)
"""


# Remove the bad samples in temperature
data = data[(data['maxTemp'] <= 110) & (data['minTemp'] >= 25)]

# List unique values on example column using drop_duplicates(We can also use unique())
df2 = pd.DataFrame(data, columns=['ZIP'])
u = df2.drop_duplicates(['ZIP'])

print(data['cloud'])

# Get data for cities
# 94107 -> San Francisco
# 94063 -> San Mateo
# 94301 -> Santa Clara
# 94041 -> Mountain View
# 95113 -> San Jose
zipcodes = [94107, 94063, 94301, 94041, 95113]

# Plots of Mean temperature in Fahrenheit scale

plt.figure()
for zcode in zipcodes:
  local = data.loc[data['ZIP'] == zcode]
  df1 = pd.DataFrame(local, columns=['meanTemp'])
  plt.plot(df1.as_matrix(), '-', label=str(zcode))
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('Temperature in Fahrenheit scale')
plt.title('Fahrenheit Mean Temperature on Bay Area Cities')
plt.legend(["San Francisco", "San Mateo","Santa Clara", "Mountain View","San Jose"])
plt.show()

# Plot compare Mean Wind and Max Gust

plt.figure()
for zcode in zipcodes:
    mw = data.loc[data['ZIP'] == zcode]
    df3 = pd.DataFrame(mw, columns=['meanWin', 'maxGust'])
    plt.plot(df3.as_matrix(),'-', label=str(zcode))
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('MPH')
plt.title('Mean Wind and Max Gust')
plt.legend(["Mean Wind","Max Gust"])
plt.show()

# Plot mean temperature with mean humidity example for San Francisco

sf = data.loc[data['ZIP'] == 94107]
plt.figure()
df4 = pd.DataFrame(sf, columns=['meanTemp','meanHum'])
plt.plot(df4, '-')
plt.grid(True)
plt.autoscale()
plt.xlabel('Days')
plt.ylabel('x')
plt.title('')
plt.legend(["Mean Temp", "Mean Humidity"])
plt.show()


# Plot Raining and Cloud Cover example for San Francisco
"""
plt.figure()
df5 = pd.DataFrame(sf, columns=['preIn','cloud'])
plt.plot(df5, '-')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('XXX')
plt.title('XXXXX')
plt.legend(["preIn","Cloud"])
plt.show()

# Plot Wind Speed and Wind Dir Degree example for San Francisco

plt.figure()
df6 = pd.DataFrame(sf, columns=['meanWind', 'WinDir'])
plt.plot(df6,'-')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('ss')
plt.title('Mean Wind and Wind Dir Degree')
plt.legend(["Mean Wind", "Wind Dir Degree"])
plt.show()
"""
# Correlation between two columns

sns.lmplot(x='meanTemp', y='meanHum', data=data)
plt.show()


# Histogram


# Pivot tables


# Heat map of Rain day per day (one year cycle)
