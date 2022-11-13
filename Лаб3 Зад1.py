import random
m = int(input())
a = []
for i in range(m):
    b = random.randint(1,99)
    a.append(b)
print(a)

for i in range(m-1):
    for j in range(m-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)