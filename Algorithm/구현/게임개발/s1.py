import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
# NxM 맵

d_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# 북 서 남 동
nr, nc, d = map(int, input().split())
# 현재위치 / 바라보고 있는 방향

matrix = [list(map(int, input().split())) for _ in range(N)]

d_cnt, cnt = 0, 0
# 한 곳에서 회전한 횟수, 총 회전한 횟수

while True:
    if d_cnt == 4: # 이미 4번 회전했으면 뒤로가자
        nr -= dr
        nc -= dc
        if matrix[nr][nc] == 1 or nr < 0 or nr >= N or nc < 0 or nc >= M:
            break
        d_cnt = 0
        continue


    d_cnt += 1
    # 회전 횟수 추가
    d = (d+1)%4
    # 회전 인덱스 + 1
    dr, dc = d_list[d]
    # 이동할 방향

    if 0 <= nr + dr < N and 0 <= nc + dc < M and matrix[nr+dr][nc+dc] == 0:
        # 맵 범위 안에 있고, 육지라면
        nr += dr    
        nc += dc
        matrix[nr][nc] = 2
        cnt += 1
        d_cnt = 0

print(cnt)