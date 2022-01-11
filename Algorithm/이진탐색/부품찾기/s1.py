import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

N = int(input())
store = list(map(int, input().split()))
M = int(input())
need = list(map(int, input().split()))

def quick_sort(args):
    if len(args) <= 1:
        return args
    pivot = args[0]
    tail = args[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

store = quick_sort(store)

def binary_search(args, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if args[mid] == target:
            return mid
        elif args[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for x in need:
    if binary_search(store, x, 0, N):
        print('Yes', end=' ')
    else:
        print('No', end=' ')