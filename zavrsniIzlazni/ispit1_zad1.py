import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.loadtxt("pima-indians-diabetes.csv", delimiter=",", skiprows=9)

print("Broj mjerenja: ", np.shape(arr)[0])

#B)
arr = arr[arr[:,5]!=0.0]
print("Broj mjerenja: ", np.shape(arr)[0])
data = pd.DataFrame(arr)
print(data.isnull().sum())
print(data.duplicated().sum())
data = data.drop_duplicates()
data = data.dropna(axis=0)
print(len(data))
data = data.reset_index(drop=True)
print(len(data))

#C)
a,b,c,d,f,bmi,e,dob,g = arr.T
plt.scatter(dob, bmi)
plt.title('Odnos dobi i BMI')
plt.xlabel('Age(years)')
plt.ylabel('BMI(weight in kg/(height in m)^2)')
plt.show()

#D)
print("max bmi: ", max(bmi))
print("min bmi: ", min(bmi))
print("Srednja vrijednost bmi: ", data[5].mean())

#E)
dija = data[data[8]==1]
print("Broj osoba s dijabetesom: ", len(dija))
print("minimalan bmi s dijabetesom: ", dija[5].min())
print("max bmi s dijabetes: ", dija[5].max())
print("srednji bmi s dijabetes: ", dija[5].mean())

no_dija = data[data[8]==0]
print("Broj osoba bez dijabetesom: ", len(no_dija))
print("minimalan bmi bez dijabetesom: ", no_dija[5].min())
print("max bmi bez dijabetes: ", no_dija[5].max())
print("srednji bmi bez dijabetes: ", no_dija[5].mean())