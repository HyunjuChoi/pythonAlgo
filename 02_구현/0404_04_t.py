n,m = map(int, input().split())

# 방문 위치 저장하기 위한 맵 생성 후 0으로 초기화 하기!!
d = [[0] * m for _ in range(n)]      # NxM 행렬 0으로 초기화

# 현재 캐릭터 x 좌표, y 좌표, 방향 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1     # 현재 좌표 방문 처리

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 start
count = 1
turn_time = 0
while True:
    # 왼쪽 회전\]
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 정면 가보지 않은 칸 존재 시 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1 
        turn_time = 0
        continue
    #회전 후 정면 가보지 않은 칸 없거나 바다인 경우
    else:
        turn_time +=1
    # 네 방향 모두 못 갈 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있을 시 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤로 바다가 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

