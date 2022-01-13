import sys
input = sys.stdin.readline

INF = 1e9  # 10억, 갈 수 없는 노드 즉 무한비용
N, M = map(int, input().split())    # 노드개수, 간선개수
start = int(input())                # 시작노드

graph = [[] for _ in range(N+1)]
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기

visited = [False]*(N+1)
# 방문한 노드 체크를 위한 리스트

distance = [INF]*(N+1)
# 최단거리 테이블 초기화

for _ in range(M):
    a, b, c = map(int,input().split())      # a 노드에서 b 노드로 가는 비용 c
    graph[a].append((b,c))                  # 연결된 노드와 비용 입력

def smallest_cost():
    '''
    방문하지 않은 노드 중에서 , 가장 최단 거리가 짧은 노드의 번호를 반환
    '''
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijstra(start):
    distance[start] = 0         # 시작노드 거리 0
    visited[start] = True       # 시작노드 방문처리
    for j in graph[start]:      # 시작노드가 연결된 곳들의 정보 j[0]: 연결노드 번호 j[1]: 비용
        distance[j[0]] = j[1]   # 연결된 노드의 거리 갱신
    
    for i in range(N-1):
        now = smallest_cost()   # =방문하지 않은 곳 중 제일 적은 비용 드는노드 번호
        visited[now] = True     # 방문처리
        for j in graph[now]:    # 현재노드가 연결된 곳들의 정보 j[0]: 연결노드 번호 j[1]: 비용
            cost = distance[now] + j[1]     # 현재위치까지의 비용 + 현재위치에서 연결된 노드로 가는 비용
            if cost < distance[j[0]]:       # 이전에 계산된 최소 비용보다 cost가 적다면
                distance[j[0]] = cost       # 갱신

dijstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
