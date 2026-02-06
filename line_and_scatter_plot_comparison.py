import matplotlib.pyplot as plt

#basic row, col to plot graph
X = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.scatter(X, y, label="scatter-points")
plt.plot(X, y, label="line-plot")
plt.legend()
plt.xlabel("Integers") #naming x-axis
plt.ylabel("Squared_Nos") #naming y-axis
plt.title("Integers vs sqaured numbers") #plot title
plt.show() #plot of x, y will be show