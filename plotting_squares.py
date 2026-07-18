import matplotlib.pyplot as plt
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
color=[10,20,30,40,50,60,70,80,90,100]
plt.scatter(a, b,c=color,s=500, marker="*", cmap="YlGnBu", edgecolors="black", linewidths=1.3)
plt.xlabel("Number", fontsize=15)
plt.ylabel("Square", fontsize=15)
plt.title("Number x Square", fontsize=20)
plt.colorbar()
plt.show()
