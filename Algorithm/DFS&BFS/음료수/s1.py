import sys
from collections import deque

sys.stdin = open('input.txt')


d_list = [(1,0), (-1,0), (0,1), (0,-1)]

def BFS(vis, ni, nj):
    queue = deque([(ni, nj)])
    vis[ni][nj] = 1
    
    while queue:
        ni, nj = queue.popleft()
        for di, dj in d_list:
            if 0 <= ni+di < N and 0 <= nj+dj < M and matrix[ni+di][nj+dj] == 0 and vis[ni+di][nj+dj] == 0:
                queue.append((ni+di, nj+dj))
                vis[ni+di][nj+dj] = 1


N, M = map(int, input().split())
# N x M 행렬

matrix = [list(map(int,input().split())) for _ in range(N)]
# 얼음 틀
visited = [[0]*M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j]==0 and visited[i][j]==0:
            BFS(visited, i, j)
            result += 1
print(result)