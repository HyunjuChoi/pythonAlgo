# 231003
# p262 전보

import sys
import heapq

input= sys.stdin.readline

INF = 1e9
n, m, c= map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)        # 최단 거리 테이블

for _ in range(m):
    x ,y ,z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q=[]
    