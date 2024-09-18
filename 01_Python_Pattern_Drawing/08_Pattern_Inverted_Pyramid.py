#Develop a Python script that prints an inverted pyramid pattern based on the number of rows provided by the user.

n = int(input())

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
