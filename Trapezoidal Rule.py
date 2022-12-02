from sympy import *
from prettytable import PrettyTable

def funcVal(func, x):
    return eval(func)

def totalArea(func, a, b, n):
    fa = funcVal(func, a)
    fb = funcVal(func, b)
    total = 0
    h = (b-a)/n

    for i in range(1, n):
        total += funcVal(func, (a+i*h))

    return (h / 2) * (fa + 2*total + fb)

func = input('Enter your function : ')
a = float(input('Lower limit : '))
b = float(input('Upper limit : '))

print('Which Trapezoidal Rule to apply?')
print('1. Single Segment')
print('2. Multiple Segment')
choice = int(input('Your choice: '))

if choice == 1:
    area = totalArea(func, a, b, 1)
    print(f"\nTotal Area (by Single Segment Trapezoidal Rule): {area}")
elif choice == 2:
    n = int(input('Number of segments: '))
    exact = float(input('Exact value of the integration: '))

    myTable = PrettyTable(['# of Segments', 'Approximate Value', 'E\N{LATIN SUBSCRIPT SMALL LETTER T}', '|\N{GREEK SMALL LETTER EPSILON}|%'])
    i = 1
    stop = int(2**4)
    flag = False
    while(i<=stop):
        if(i>n and flag==False):
            area = totalArea(func, a, b, n)
            print(f"\nTotal Area for {n} Segment (by Multiple Segment Trapezoidal Rule): {area}")
            flag = True
            myTable.add_row([n, round(area, 3), round((exact - area), 3), round((abs(exact - area) / exact) * 100, 3)])
        else:
            area = totalArea(func, a, b, i)
            if(i!=n):
                myTable.add_row([i, round(area,3), round((exact-area), 3), round((abs(exact-area)/exact)*100, 3)])
            i*=2
    if(stop<n):
        area = totalArea(func, a, b, n)
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