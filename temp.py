import matplotlib.pyplot as plt
import numpy as np
y = [] 
for i in range (1,20):
   x= i+1
   y.append(x)
z =np.random.rand(19)
plt.plot(y, z) 
plt.xlabel("y")
plt.ylabel("z")
plt.show()

 

