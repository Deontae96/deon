import matplotlib.pyplot as plt
import numpy as np

plt.plot(range(1,50),range(1,50))
#plt.plot(range(50,1),range(50,1))
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("This is a line")
plt.show()


plt.plot([1,2,3],[2,4,1],label = "line 1") #Split the graph into arrays
plt.plot([1,2,3],[4,1,3.5], label = "line 2")
plt.legend()
plt.show()
