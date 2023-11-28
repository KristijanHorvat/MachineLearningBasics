import pandas as pd

data = pd.read_csv("data_C02_emission.csv")

print(len(data))
print(data.info())
print("izostale vrijednosti "+str(data.isnull().sum()))
data.drop_duplicates()
data = data.reset_index(drop=True)
data['Make'] = data['Make'].astype("category")
data['Model'] = data['Model'].astype("category")
data['Vehicle Class'] = data['Vehicle Class'].astype("category")
data['Transmission'] = data['Transmission'].astype("category")
data['Fuel Type'] = data['Fuel Type'].astype("category")
data.info()

data.sort_values(by="Fuel Consumption City (L/100km)",
                 ascending=True, inplace=True)
print(data.head(3)[["Make", "Model", "Fuel Consumption City (L/100km)"]])
print(data.tail(3)[["Make", "Model", "Fuel Consumption City (L/100km)"]])
new_data = data[(data["Engine Size (L)"] > 2.5) &
                (data["Engine Size (L)"] < 3.5)]
print(new_data.count())
print(new_data["CO2 Emissions (g/km)"].mean())

audi = data[(data["Make"] == "Audi")]
print(audi.count())
audi2 = audi[(data["Cylinders"] == 4)]
print(audi2["CO2 Emissions (g/km)"].mean())

for i in range(4, 17, 2):
    print(len(data[(data["Cylinders"] == i)]))
    print(data[(data["Cylinders"] == i)]["CO2 Emissions (g/km)"].mean())

print(data[(data["Fuel Type"] == 'D')]
      ["Fuel Consumption City (L/100km)"].mean())
print(data[(data["Fuel Type"] == 'X')]
      ["Fuel Consumption City (L/100km)"].mean())
print(data[(data["Fuel Type"] == 'D')]
      ["Fuel Consumption City (L/100km)"].median())
print(data[(data["Fuel Type"] == 'X')]
      ["Fuel Consumption City (L/100km)"].median())

car = data[(data["Cylinders"] == 4) & (data["Fuel Type"] == 'D')]
car.sort_values(by="Fuel Consumption City (L/100km)",
                ascending=True, inplace=True)
print(car.head(1))

print(len(data[(data["Transmission"] == 'M')]))

print(data.corr(numeric_only=True))
