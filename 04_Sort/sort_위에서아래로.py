n = int(input())

array = []

for i in range(n):
    num = int(input())
    array.append(num)

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')