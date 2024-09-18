#Write a Python script that prints a square pattern where stars and dashes alternate in each row.

n = int(input())

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print("-", end="")
    print()
