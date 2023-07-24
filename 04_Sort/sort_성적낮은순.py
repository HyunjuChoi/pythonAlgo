n = int(input())

array = []

for i in range(n):
    array.append(list(map(str, input().split())))

#print(array)

def score(data):
    return int(data[1])

array = sorted(array, key=score)

for i in range(len(array)):
    print(array[i][0], end=' ')