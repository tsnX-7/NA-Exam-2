from prettytable import PrettyTable
import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))
x = []
y = []

myTable = PrettyTable(['#', 'x', 'y', 'x\N{SUPERSCRIPT TWO}', 'xy'])
for i in range(0, n):
    data = input("x y {} : ".format(i+1)).split()
    x.append(float(data[0]))
    y.append(float(data[1]))

sum_x = sum_xy = sum_x2 = sum_y = 0

for i in range(0, n):
    sum_x += x[i]
    sum_y += y[i]
    sum_x2 += x[i]**2
    sum_xy += x[i]*y[i]
    myTable.add_row([i+1, x[i], y[i], round(x[i]**2, 6), round(x[i]*y[i], 6)])

myTable.add_row(["\N{GREEK CAPITAL LETTER SIGMA}", round(sum_x,6), round(sum_y,6), round(sum_x2, 6), round(sum_xy, 6)])
avg_x = sum_x / n
avg_y = sum_x / n

a1 = ((n * sum_xy) - (sum_x*sum_y)) / ((n*sum_x2)-(sum_x**2))
a0 = ((sum_x2*sum_y)-(sum_x*sum_xy))/((n*sum_x2)-(sum_x**2))
print(myTable)
print("\n\n")
print("The Linear Regression Model for the given data points: y = (%.3f) + (%.3f)x" % (a0, a1))

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Model")
y_val = []
for i in range(n):
    y_val.append(a0 + a1 * x[i])
plt.plot(x, y_val, color="y")
plt.show()

'''
5
0.698132 0.188224
0.959931 0.209138
1.134464 0.230052
1.570796 0.250965
1.919862 0.313707
'''