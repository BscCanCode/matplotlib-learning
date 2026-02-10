import matplotlib.pyplot as plt

#class A
hours = [1, 2, 3, 4, 5, 6]
score = [50, 55, 60, 65, 70, 80]

plt.scatter(hours, score, color = "red", label = "scatter_plot")
plt.xlabel("Student studied this much hour")
plt.ylabel("Student scored")
plt.legend()
plt.grid()
plt.title("Student marks based on hours od study")
plt.show()

#plotting multiple data
#class A and Class B 

plt.scatter([1, 2, 3], [34, 56, 78], label="class_A")
plt.scatter([1, 2, 3], [43, 32, 65], label = "Class_B")

plt.xlabel("Hours studied")
plt.ylabel("Marks gained")
plt.legend()
plt.title("Hours study vs marks scored data of class A and class B")
plt.grid()
plt.show()