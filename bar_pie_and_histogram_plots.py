import matplotlib.pyplot as plt 

X = ['A', 'B', 'C', 'D']
y = [1200, 3400, 321, 4345]

#plotting a bar chart
plt.bar(X, y, width=0.5, label="BAr_chart")
plt.xlabel("product")
plt.ylabel("Sales")
plt.legend()
plt.title("Product vs sales")
plt.show()

#plotting a piechart
plt.pie(y, labels=X, autopct='%1.1f%%')
plt.legend()
plt.show()


#plotting a histogram
score = [23, 45, 56, 23, 67, 89, 98, 76, 65, 54, 43, 65, 78, 98, 56, 34]
plt.hist(score, bins=5, color="black", edgecolor="white")
plt.xlabel("Score of student")
plt.ylabel("No. of student")
plt.title("Score distribution")
plt.show()

