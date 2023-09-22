# 230922
# 이코테 p259 미래도시

INF = int(1e9)

# 전체 회사 개수와 경로 개수 입력
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 연결된 두 회사 번호 공백으로 구분해 입력
for i in range(m+1):
    a, b = map(int, input().split())
    graph[i].append((a,b))
# 도착회사, 중간에 방문할 곳    
x, k = map(int, input().split())

