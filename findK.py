def find_k_min(nums, k):
    result = list()
    max_pointer = 0
    max_num = nums[max_pointer]
    result.append(max_num)
    for i in nums[1:]:
        if k > result.__len__():
            result.append(i)
        else:
            if i < max_num:
                result[max_pointer] = i
                max_num = max(result)
                max_pointer = result.index(max_num)
    else:
        return result
