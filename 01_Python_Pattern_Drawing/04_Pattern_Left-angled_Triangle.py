#Design a Python code snippet to print a left-angled triangle pattern.

n = int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
