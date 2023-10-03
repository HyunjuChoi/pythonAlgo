# 230922
# 이코테 p259 미래도시

INF = int(1e9)

# 전체 회사 개수와 경로 개수 입력
n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 연결된 두 회사 번호 공백으로 구분해 입력 후 1로 초기화(비용 무조건 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# 도착회사, 중간에 방문할 곳    
x, k = map(int, input().split())

# 점화식에 따른 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 수행결과
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)