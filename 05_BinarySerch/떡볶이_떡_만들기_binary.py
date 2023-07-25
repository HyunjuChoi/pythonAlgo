#230725

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 반복 수행
result = 0
while(start < end):
    total = 0
    mid = (start+ end) // 2
    for x in array:
        if x > mid:     # 배열 값이 중간값(빼야하는 값 = h 값)보다 클 때만 
                        # total에 더함 (아니면 -값 더해지므로!)
            total += x - mid
    if total < m:       # 떡볶이 다 자른 후 더한 값이 원하는 값(m)보다 작으면 
        end = mid - 1  # 더 길게 잘라야 하므로 mid 값(h) 감소
    else:
        result = mid    # 최대한 덜 잘랐을 때가 정답이므로 여기서 result 기록
        start = mid +1  # 떡볶이 길이가 더 길면 더 짧게 잘라야 하므로 mid 값(h) 증가

print(result)