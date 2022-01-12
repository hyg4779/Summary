import sys
sys.stdin = open('input.txt')

nums = [int(input()) for _ in range(int(input()))]

for i in range(len(nums)-1, -1, -1):
    max_index = i

    for j in range(len(nums)-1, i, -1):
        if nums[j] > nums[max_index]:
            nums[max_index], nums[j] = nums[j], nums[max_index]

print(nums)