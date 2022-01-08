import sys
sys.stdin = open('input.txt')

now_c, now_r = input()

convertor = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8}
now_r = int(now_r)
now_c = convertor[now_c]

matrix = [list(range(9)) for _ in range(9)]
# 8x8 체스판

verticle_move = [(2, 1),(2, -1),(-2, 1),(-2, -1)]
horizon_move= [(1, 2),(1, -2),(-1, 2),(-1, -2)]
# 수직으로 2칸이동 + 수평으로 1칸이동  / 수평으로 2칸이동 + 수직으로 1칸이동

cnt = 0

for r,c in verticle_move:

    if 1 <= now_r + r <= 8 and 1 <= now_c + c <= 8:
        cnt += 1
for r,c in horizon_move:
    if 1 <= now_r + r <= 8 and 1 <= now_c + c <= 8:
        cnt += 1

print(cnt)