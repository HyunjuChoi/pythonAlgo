n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

#print(array)

result = -1

d = [0]*10001

d[0] = array[0]

for i in range(1, m):
    while (d[i] <= m):
        d[i] = min(d[i-1]*2, array[i])
    break

print(result)