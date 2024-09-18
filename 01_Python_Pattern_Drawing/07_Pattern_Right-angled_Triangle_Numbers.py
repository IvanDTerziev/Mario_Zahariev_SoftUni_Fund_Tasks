#Write a Python program that prints a right-angled triangle using numbers.

n = int(input())
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()