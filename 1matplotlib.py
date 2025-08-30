import matplotlib.pyplot as plt
x=[1,3,5,7,9]
y=[20,4,6,8,10]

plt.plot(x,y)
plt.title("basic line graph")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.show()

import matplotlib.pyplot as plt
x=["a","b","c"]
y=[1,2,3]
plt.bar(x,y,color="red")
plt.title("bar plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

import matplotlib.pyplot as plt
x=[1,3,5,7,9]
y=[20,4,6,8,10]
plt.scatter(x,y,color="green",marker="8")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.show()