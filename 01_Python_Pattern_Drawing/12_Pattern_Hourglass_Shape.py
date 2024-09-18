#Design a Python program to display an hourglass shape.

n = int(input())

for i in range(n + 1):
    if i % 2 == 0:
        print('*-*-*')
    else:
        print('-*-*-')
