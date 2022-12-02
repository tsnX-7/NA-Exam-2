from sympy import *
from prettytable import PrettyTable

def funcVal(func, x):
    val = eval(func)
    return val

def twoSegTotalArea(func, a, b):
    fa = funcVal(func, a)
    fb = funcVal(func, b)
    m = (a+b)/2
    fm = funcVal(func, m)
    h = (b-a)/2
    return (h/3) * (fa + 4*fm + fb)

def mulSegTotalArea(func, a, b, n):
    h = (b-a)/n
    fval = []
    seg = a
    while (seg <= b):
        val = funcVal(func, seg)
        fval.append(val)
        seg += h

    odd = 0
    for i in range(1, n, 2):
        odd += fval[i]

    even = 0
    for i in range(2, n - 1, 2):
        even += fval[i]

    result = (h / 3) * (fval[0] + 4 * odd + 2 * even + fval[n])
    return result

func = input('Enter your function : ')
a = float(input('Lower limit : '))
b = float(input('Upper limit : '))

print("Which Simpson's 1/3rd Rule to apply?")
print('1. 2 Segment')
print('2. Multiple Segment')
choice = int(input('Your choice: '))

if choice == 1:
    area = twoSegTotalArea(func, a, b)
    print(f"\nTotal Area (by 2-Segment Simpson's 1/3rd Rule): {area}")

elif choice == 2:
    n = int(input('Number of Segment(must be even): '))
    if n%2!=0:
        raise Exception('Invalid no. of segment')
    exact = float(input('Exact solution to the integration: '))
    myTable = PrettyTable(['# of Segments', 'Approximate Value', 'E\N{LATIN SUBSCRIPT SMALL LETTER T}', '|\N{GREEK SMALL LETTER EPSILON}|%'])
    i = 1
    stop = int(2 ** 4)
    flag = False
    while (i <= stop):
        if (i > n and flag == False):
            area = mulSegTotalArea(func, a, b, n)
            print(f"\nTotal Area for {n} Segment (by Multiple Segment Simpson's 1/3rd Rule): {area}")
            flag = True
            myTable.add_row([n, round(area, 3), round((exact - area), 3), round((abs(exact - area) / exact) * 100, 3)])
        else:
            area = mulSegTotalArea(func, a, b, i)
            if i!=n:
                myTable.add_row([i, round(area, 3), round((exact - area), 3), round((abs(exact - area) / exact) * 100, 3)])
            i *= 2
    if (stop < n):
        area = mulSegTotalArea(func, a, b, n)
        print(f"\nTotal Area for {n} Segments (by Multiple Segment Trapezoidal Rule): {area}")
        myTable.add_row([n, round(area, 3), round((exact - area), 3), round((abs(exact - area) / exact) * 100, 3)])

    print('\nComparison Table for different no. of segment in Trapezoidal Rule: ')
    print(myTable)
else:
    raise Exception('Invalid Choice')


'''
2000*ln(140000/(140000-2100*x))-9.8*x
8
30
1

2000*ln(140000/(140000-2100*x))-9.8*x
8
30
2
4
11061
'''