import random
def numbers():
    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(list_)
    return n
n = numbers()

result = []
m = 0
for i in range(1, n):
    m = m + 1
    for j in range(m, n):
        if i == j:
            continue
        elif n % (i + j) == 0:
            result.append(i)
            result.append(j)

print(n)
print(*result)