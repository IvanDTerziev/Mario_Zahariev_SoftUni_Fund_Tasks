#Craft a Python script to print a mirrored right-angled triangle pattern.

n = int(input());
k = 8
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()