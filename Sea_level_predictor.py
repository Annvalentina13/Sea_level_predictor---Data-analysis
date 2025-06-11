import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the data
data = pd.read_csv('flat-ui__data-Wed Jun 11 2025.csv')
# Check if the data is loaded correctly
print(data.head())


# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

# Perform linear regression on entire dataset
slope_all, intercept_all, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

# Predict values through 2050
years_extended = pd.Series(range(1880, 2051))
sea_level_pred_all = intercept_all + slope_all * years_extended

# Plot line of best fit for entire dataset
plt.plot(years_extended, sea_level_pred_all, 'r', label='Best Fit Line (All Data)')

# Create data subset for year >= 2000
data_recent = data[data['Year'] >= 2000]

# Perform linear regression on recent data
slope_recent, intercept_recent, r_value, p_value, std_err = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

# Predict values through 2050 for recent data
sea_level_pred_recent = intercept_recent + slope_recent * years_extended

# Plot line of best fit for recent data
plt.plot(years_extended, sea_level_pred_recent, 'green', label='Best Fit Line (2000-Present)')

# Plot labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
