import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

'''
n개 도시, 도시간 단방향 연결, 통로마다 시간소요 상이
도달하는 도시 수, 모두 메세지 받는 시간
'''

# N개 도시, M개 통로, 출발도시 C
N, M, C =  map(int, input().split())

INF = int(1e9)

# 도시 연결 인접행렬
way = [[]*(N+1) for _ in range(N+1)]

# 도시간 거리 무한대로 초기화
dist = [INF]*(N+1)

# 방문노드
visited = [False]*(N+1)

# 연결되어 있는 (도시, 비용) 추가
for _ in range(M):
    a, b, c = map(int, input().split())
    way[a].append((b,c))

def smallest_cost():
    '''
    방문하지 않은 노드 중, 가장 최단거리 짧은 노드의 번호 반환
    '''
    min_v = INF
    index = 0
    for i in range(1, N+1):
        if dist[i] < min_v and not visited[i]:
            min_v = dist[i]
            index = i
    return index


def dijstra(start):
    dist[start] = 0
    visited[start] = True
    for j in way[start]:
        dist[j[0]] = j[1]

    for k in range(N-1):
        now = smallest_cost()
        visited[now] = True
        for l in way[now]:
            cost = dist[now] + l[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost
    return dist


dist = dijstra(C)

result = list()

for m in dist:
    if m != INF and m != 0:
        result.append(m)

print(max(result), len(result))
