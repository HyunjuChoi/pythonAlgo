# 230921
# 플로이드 워셜

INF = int(1e9)

# 노드, 간선 개수 입력
n, m = map(int, input().split())
# 2차원 리스트(그래프) 생성, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 노드 0으로 초기화
for a in (1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 후 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없을 때 "Infinity" 출력
        if graph[a][b] == INF:
            print("Infinity", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()