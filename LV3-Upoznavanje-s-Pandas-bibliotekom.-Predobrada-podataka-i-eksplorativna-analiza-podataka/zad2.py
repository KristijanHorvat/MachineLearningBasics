import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data_C02_emission.csv')
for col in data.select_dtypes(include='object'):
    data[col] = data[col].astype('category')

plt.figure()
data['CO2 Emissions (g/km)'].plot(kind='hist', bins= 50)
data.plot.scatter(x = 'Fuel Consumption City (L/100km)', y = 'CO2 Emissions (g/km)', c='Fuel Type', cmap='hot', s=50)

data.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')

plt.figure()
grouped = data.groupby('Fuel Type').size()
grouped.plot(kind='bar')

plt.figure()
data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().plot(kind='bar')

plt.show()
