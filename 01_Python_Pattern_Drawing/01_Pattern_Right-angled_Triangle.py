#Develop a Python script that generates a right-angled triangle pattern.

n = int(input())
for i in range(1, n + 1):

    for j in range(i):
        print('*', end='')

    print()
