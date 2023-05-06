import numpy as np
import matplotlib.pyplot as plt 

zeros = np.zeros((50,50))
ones = np.ones((50,50))
lm = np.vstack((zeros,ones))
rm = np.vstack((ones, zeros))
m = np.hstack((lm,rm))

plt.figure()
plt.imshow(m, cmap='gray')
plt.show()
