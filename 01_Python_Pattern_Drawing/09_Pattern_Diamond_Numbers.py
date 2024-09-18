#Write a Python program that prints a diamond shape pattern with numbers.

n = int(input())

for i in range(1, n):
    print((n-i)*' ', end='')
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

for i in range(n, 0, -1):
    print((n-i)*' ', end='')
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
