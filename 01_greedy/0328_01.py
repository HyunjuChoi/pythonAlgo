n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0
cnt = 0

#print(data)
'''
for i in range(n):
    for j in range(k):
        result += 
'''

while(cnt != m):
    for _ in range(k):
        result += data[0]
        cnt += 1
    #if(cnt == m): break
    result += data[1]
    cnt += 1
'''

while True:
    if cnt == m:
        break
    for _ in range(k):
        result += data[0]
        cnt += 1
    if cnt == m:
        break
    result += data[1]
    cnt += 1
'''
print(result)
