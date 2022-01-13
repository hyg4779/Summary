import heapq
import sys
input = sys.stdin.readline

INF = 1e9  # 10억, 갈 수 없는 노드 즉 무한비용
N, M = map(int, input().split())    # 노드개수, 간선개수
start = int(input())                # 시작노드

graph = [[] for _ in range(N+1)]
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기

distance = [INF]*(N+1)
# 최단거리 테이블 초기화

for _ in range(M):
    a, b, c = map(int,input().split())      # a 노드에서 b 노드로 가는 비용 c
    graph[a].append((b,c))                  # 연결된 노드와 비용 입력

def dijstra(start):
    '''
    방문하지 않은 노드 중에서 , 가장 최단 거리가 짧은 노드의 번호를 반환
    '''
    q = []
    heapq.heappush(q, (0, start))
    # 시작 노드로 가는 경로는 0으로 설정 후 q에 삽입
    distance[start] = 0
    while q:        # q가 비어있지 않으면 반복
        dist, now = heapq.heappop(q)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:
            continue
        # 처리된 적 있는 노드는 무시
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                # 현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 더 짧은경우 갱신


dijstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
