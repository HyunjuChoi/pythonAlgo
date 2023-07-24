
def find_target(array, target, start, end):
    if start > end :
        return 'no'
    mid = (start+end) // 2
    
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return find_target(array, target, start, mid-1)
    else:
        return find_target(array, target, mid+1, end)
    

n = int(input())
array = list(map(int, input().split()))
array = sorted(array)
#print(sorted(array))

m = int(input())
target = list(map(int, input().split()))

#print(target)

for i in range(m):
    print(find_target(array, target[i], 0, n-1))
