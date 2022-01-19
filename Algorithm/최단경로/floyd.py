INF = int(1e9)

# n, m = 노드개수, 간선개수
n = int(input())
m = int(input())

# 인덱스 값을 쉽게 생각하기 위해 n+1 x n+1 배열, 모든 값 무한으로초기화
matrix = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로는 0으로 치환
for i in range(1, n+1):
    matrix[i][i] = 0

# 간선 정보 그래프에 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

# 점화식에 따라 플루이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

# 결과 출력
for r in range(1, n+1):
    for c in range(1, n+1):
        if matrix[r][c] == INF:
            print('INFINITY', end=' ')
        else:
            print(matrix[r][c], end=' ')
    print()