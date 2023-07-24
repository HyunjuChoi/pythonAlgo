#230724

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

print(array)
result = 0
target = array[0]-1

print(target)

while(1):
    if result == m:
        break
    for i in range(n):
        if result == m:
            break
        if array[i] - target >=0: 
            result += array[i] - target
    target-=1
        
print(target)