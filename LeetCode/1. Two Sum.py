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
    ## 문제 풀때 어려웠던 부분은 중복처리를 어떻게 해결해야할까? 엿다.
    ## 해결법은 애초에 딕셔너리에 넣기전에 딕셔너리 내의 값으로 계산이 되는지 확인하고 넣는것이었다.
    ## 그렇게 함으로써 중복 숫자가 나오더라도 상관없게 되었다. 기존에 딕셔너리에 값을 다 추가하고 계산하는 것과는 다르게
    ## target 값이 나오지 않으면 중복 숫자가 있던 말든 상관 없게 된다.
    
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