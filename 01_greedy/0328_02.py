
n, m = map(int, input().split())

for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    #print(min(data))
    if min_val < min(data):
        min_val = min(data)

print(min_val)