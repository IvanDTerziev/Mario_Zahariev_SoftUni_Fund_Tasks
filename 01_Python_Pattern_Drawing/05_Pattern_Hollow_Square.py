#Implement a Python program that prints a square pattern with a hollow center, where the user specifies the size of the square.

n = int(input())
print("*" * n)

for i in range(n - 2):
    print("*" + " " * (n - 2) + "*")
print("*" * n)
