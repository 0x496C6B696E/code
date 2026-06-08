<<<<<<< HEAD
x = int(input())
y = int(input())
z = int(input())
n = int(input())
=======
x = int(input("Input x: "))
y = int(input("Input y: "))
z = int(input("Input z: "))
n = int(input("Input n: "))
>>>>>>> refs/remotes/origin/main

total = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
<<<<<<< HEAD
            if (i + j+ k) != n:
                total.append([i, j, k])
print(total)
=======
            if (i + j + k) != n:
                total.append([i, j, k])
print(total)
>>>>>>> refs/remotes/origin/main
