import sys
sys.stdin = open('input.txt')


def dfs(k, visit, i, j):
    global min_cnt
    if k > min_cnt:
        return
    if i == N-1 and j == M-1:
        min_cnt = min(k, min_cnt)
        return

    for di, dj in d_list:
        if 0 <= i+di < N and 0 <= j+dj < M and matrix[i+di][j+dj]==1 and visit[i+di][j+dj] == 0:
            visit[i + di][j + dj] = 1
            dfs(k+1, visit, i+di, j+dj)
            visit[i + di][j + dj] = 0


N, M = map(int, input().split())
# N x M 미로

matrix = [list(input()) for _ in range(N)]
# 미로
visited = [[0]*M for _ in range(N)]
min_cnt = N*M

d_list = [(1,0), (-1,0), (0,1), (0,-1)]
dfs(1, visited, 0, 0)
print(min_cnt)