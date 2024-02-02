def longestConsecutive(self, nums: list[int]) -> int:
    # 시간복잡도 O(n)
    num_dict = {}
    max_count = 1
    if len(nums) == 0:
        return 0
    for i in nums :
        num_dict[i] = 1
    for i in nums :
        if i - 1 not in num_dict :
            count = 1
            while i + 1 in num_dict :
                count += 1
                i += 1
        if count > max_count :
            max_count = count
    return max_count
    
    # 시간복잡도 O(nlogn)
    nums.sort()
    max_count = 1
    count = 1
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)) :
        if nums[i] != nums[i - 1] :
            if nums[i] - nums[i - 1] == 1 :
                count += 1
            else :
                count = 1
            if max_count < count :
                    max_count = count
    return max_count


