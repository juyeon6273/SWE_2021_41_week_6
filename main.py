from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_blank = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target-num
        
        if complement in num_blank:
            return [num_blank[complement], i]
        num_blank[num] = i
    return []

input_str = input("Input: ")
input_str = input_str.replace("nums = ", "")
input_str = input_str.replace("target = ", "")
nums_str, target_str = input_str.split(", ")
nums = list(map(int, nums_str[1:-1].split(",")))
target = int(target_str.strip())

output = twoSum(nums, target)
print("Output:", "[" + ",".join(map(str, output)) + "]")
