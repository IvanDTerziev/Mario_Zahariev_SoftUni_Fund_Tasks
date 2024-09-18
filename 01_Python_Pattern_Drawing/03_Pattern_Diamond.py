#Write a Python script that displays a diamond pattern based on the number of rows (height) specified by the user.

n = int(input())
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
