#230724

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:        # array[mid]값 찾았을 때
        return mid
    elif array[mid] > target:       # array[mid]값이 target보다 클 때 
        return binary_search(array, target, start, mid-1)
    else:                           # array[mid] 값 target보다 작을 때
        return binary_search(array, target, mid+1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
    
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소 존재 X")
else:
    print(result + 1)