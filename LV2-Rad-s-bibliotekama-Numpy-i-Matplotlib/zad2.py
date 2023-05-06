import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("data.csv", delimiter=",", dtype=float, skiprows=1)

spol, visina, masa = arr.T
plt.scatter(visina, masa)
plt.scatter(visina[0:-1:50], masa[0:-1:50])
plt.xlabel("visina")
plt.ylabel("masa")
#plt.show()
print(arr.shape)
print(max(visina))
print(min(visina))
print(np.mean(visina))

m = (arr[:,0]==1)
z=(arr[:,0]==0)

print(arr[m,1].min())
print(arr[m,1].max())
print(arr[m,1].mean())