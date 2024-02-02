def twoSum(self, nums: list[int], target: int) -> list[int]:
    # 완전 탐색  # 1670ms
    for i in range(len(nums)):
            for j in range(i + 1,len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i,j]
                
    # 해시테이블 (딕셔너리) # Best runtime  #54ms
    num_dict = {}
    for idx, val in enumerate(nums) :
        find_num = target - val
        if find_num in num_dict :
            return [idx, num_dict[find_num]]
        else :
            num_dict[val] = idx
    
    # 이분탐색/이진 탐색(Binary Search)  #69ms
    nums = [[n, i] for i, n in enumerate(nums)]
    nums.sort(key = lambda x: x[0])
    l, r = 0, len(nums) - 1

    while l <= r:
        num_sum = nums[l][0] + nums[r][0]
        if num_sum == target:
            return [nums[l][1], nums[r][1]]
        elif num_sum > target:
            r -= 1
        else:
            l += 1