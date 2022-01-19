'''
판매원A씨 / 1번부터 n번의 회사 / 특정회사끼리 양방향 연결
A씨 현재 1번회사 / X번 회사에 방문해야함
회사간 거리는 모두 1
소개팅 상대는 K회사
A씨 경로 1 > K > X
최단경로는?
간선개수 7개
V, E = 5, 7
K, X = 4, 5
1 2 1 3 1 4 2 4 3 4 3 5 4 5
'''

import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

INF = int(1e9)
# 정점수, 간선수
V, E = map(int, input().split())


# 간선 정보 담는 리스트
road = [[INF]*(V+1) for _ in range(V+1)]

# 자기자신으로 경로 0
for i in range(1, V+1):
    road[i][i] = 0

# road 연결 초기화
for j in range(E):
    a, b = map(int, input().split())
    road[a][b] = 1
    road[b][a] = 1

# 플루이드 워셜
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            road[i][j] = min(road[i][j], road[i][k] + road[k][j])

# 경유지, 목적지
X, G = map(int, input().split())

result = road[1][G] + road[G][X]

print(result)