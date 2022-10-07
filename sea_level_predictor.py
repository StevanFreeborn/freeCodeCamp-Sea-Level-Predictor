import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  y = df['CSIRO Adjusted Sea Level']
  x = df['Year']

  # Create scatter plot
  fix, ax = plt.subplots()
  plt.scatter(x, y)

  end_year = 2051
  
  # Create first line of best fit
  res = linregress(x, y)
  x_pred = pd.Series([i for i in range(1880, end_year)])
  y_pred = res.slope * x_pred + res.intercept
  plt.plot(x_pred, y_pred, 'r')
  
  # Create second line of best fit
  start_year = 2000
  df_filtered = df[df['Year'] >= start_year]
  x_filtered = df_filtered['Year']
  y_filtered = df_filtered['CSIRO Adjusted Sea Level']
  res_filtered = linregress(x_filtered, y_filtered)
  x_pred_filtered = x_pred = pd.Series([i for i in range(start_year, end_year)])
  y_pred_filtered = res_filtered.slope * x_pred_filtered + res_filtered.intercept
  plt.plot(x_pred_filtered, y_pred_filtered, 'green')

  # Add labels and title
  ax.set_title("Rise in Sea Level")
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()