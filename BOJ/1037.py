# Bronze

from sys import stdin

n = int(stdin.readline().rstrip())

nums = list(map(int, stdin.readline().rstrip().split()))
nums.sort()
print(nums[-1]*nums[0])