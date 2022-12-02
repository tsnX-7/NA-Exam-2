from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

def gaussian_partial_pivoting(mat, n):
    step = 1
    for i in range(0, n - 1):
        max_row, val = i, 0
        for j in range(i, n):
            if (abs(mat[j][i]) > val):
                val = abs(mat[j][i])
                max_row = j

        for k in range(0, n + 1):
            mat[i][k], mat[max_row][k] = mat[max_row][k], mat[i][k]

        for j in range(i + 1, n):
            try:
                val = mat[j][i] / mat[i][i]
            except:
                print("Division By Zero Error. Couldn't find sol")
                return False

            for k in range(i, n+1):
                mat[j][k] -= (val * mat[i][k])
    sol = [0 for k in range(n)]

    for i in range(n - 1, -1, -1):
        try:
            sol[i] = mat[i][n] / mat[i][i]
        except:
            print("Division By Zerro Error. Couldn't find sol")
            return False

        for j in range(i - 1, -1, -1):
            mat[j][n] -= (mat[j][i] * sol[i])
    return sol

def Direct_interpolation(data, val):
    mat1 = [[0.0 for j in range(3)] for i in range(2)]
    mat2 = [[0.0 for j in range(4)] for i in range(3)]
    mat3 = [[0.0 for j in range(5)] for i in range(4)]

    ans1 = -1

    if (len(data) >= 2):
        for i in range(2):
            mat1[i][0] = 1  # a0
            mat1[i][1] = data[i][1]  # a1 = x
            mat1[i][2] = data[i][2]  # f(x)
        sol1 = gaussian_partial_pivoting(mat1, 2)
        ans1 = sol1[0] + sol1[1] * val

    ans2 = -1
    ans3 = -1

    if (len(data) >= 3):
        for i in range(3):
            mat2[i][0] = 1  # a0
            mat2[i][1] = data[i][1]  # a1 = x
            mat2[i][2] = data[i][1] * data[i][1]  # a2=x^2
            mat2[i][3] = data[i][2]  # f(x)

        sol = gaussian_partial_pivoting(mat2, 3)

        ans2 = sol[0] + sol[1] * val + sol[2] * val * val

    if (len(data) >= 4):
        for i in range(4):
            mat3[i][0] = 1  # a^0
            mat3[i][1] = data[i][1]  # a^1
            mat3[i][2] = data[i][1]**2 # a^2=x^2
            mat3[i][3] = data[i][1]**3  # a^3=x^3
            mat3[i][4] = data[i][2]  # f(x)

        sol = gaussian_partial_pivoting(mat3, 4)

        ans3 = sol[0] + sol[1] * val + sol[2] * val * val + sol[3] * val * val * val
        error1 = abs(ans1 - ans2) / ans2
        error2 = abs(ans2 - ans3) / ans3

    my_table.add_row(["Direct Interpolation", str(str(ans1) + "\n" + "---"), str(str(ans2) + "\n" + str(error1) + "%"),
                      str(str(ans3) + "\n" + str(error2) + "%")])

def do_lagrange(x, y, val):
    ans = 0
    n = len(x)
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (val - x[j]) / (x[i] - x[j])

        ans += y[i] * l
    return ans


def Lagrange_method(data, val):
    # linear interpolation
    x = [data[0][1], data[1][1]]  # closest 2 data points
    y = [data[0][2], data[1][2]]  # closest 2 data points

    ans1 = do_lagrange(x, y, val)

    # quadratic nterpolation
    x.append(data[2][1])
    y.append(data[2][2])

    ans2 = do_lagrange(x, y, val)

    # qubic interpolation
    x.append(data[3][1])
    y.append(data[3][2])

    ans3 = do_lagrange(x, y, val)

    error1 = abs(ans1 - ans2) / ans2
    error2 = abs(ans2 - ans3) / ans3

    my_table.add_row(["Lagrange method", str(str(ans1) + "\n" + "---"), str(str(ans2) + "\n" + str(error1) + "%"),
                      str(str(ans3) + "\n" + str(error2) + "%")])


def do_newton_divided(x, y, val):
    n = len(x)

    data_table = [[0.0 for j in range(n)] for i in range(n)]

    for i in range(n):
        data_table[i][0] = y[i]

    for j in range(n - 1):
        for i in range(j + 1, n):
            data_table[i][j + 1] = (data_table[i][j] - data_table[j][j]) / (x[i] - x[j])

    ans = data_table[0][0]

    for i in range(n - 1):
        tmp = 1
        for j in range(i + 1):
            tmp *= (val - x[j])
        ans += tmp * data_table[i + 1][i + 1]
    return ans


def newtons_divided_difference(data, val):
    # Linear newtons divided
    x = [data[0][1], data[1][1]]  # closest 2 data points
    y = [data[0][2], data[1][2]]  # closest 2 data points

    ans1 = do_newton_divided(x, y, val)

    # quadratic newtons divided
    x.append(data[2][1])
    y.append(data[2][2])

    ans2 = do_newton_divided(x, y, val)

    # qubic newtons divided
    x.append(data[3][1])
    y.append(data[3][2])

    ans3 = do_newton_divided(x, y, val)

    error1 = abs(ans1 - ans2) / ans2
    error2 = abs(ans2 - ans3) / ans3

    my_table.add_row(
        ["Newtons divided method", str(str(ans1) + "\n" + "---"), str(str(ans2) + "\n" + str(error1) + "%"),
         str(str(ans3) + "\n" + str(error2) + "%")])

number_of_data_points = int(input("Enter the number of data points: "))

print("Enter the data points x f(x) format seperated by space")

x = []
y = []

for i in range(0, number_of_data_points):
    data = input(" x f(x) {} : ".format(i + 1)).split()
    x.append(float(data[0]))
    y.append(float(data[1]))

val = float(input("Enter x at which you want to find value of the function \n"))

my_table = PrettyTable(['Method Name', "Linear with Error(%)", "Quadratic with Error(%)", "Qubic with Error(%)"])

data = []
for i in range(number_of_data_points):
    data.append([abs(val - x[i]), x[i], y[i]])

data.sort()
Direct_interpolation(data, val)
Lagrange_method(data, val)
newtons_divided_difference(data, val)

print(my_table)
plt.scatter(np.array(x), np.array(y))
plt.title("Scatter plot of the data")
plt.xlabel("X")
plt.ylabel("F(X)")
plt.show()