class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index,val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                return [index, hashMap[diff]]
            hashMap[val] = index

"""
Created empty hashmap
enumerate() gives both the index and value.
Needed Number = Target - Current Number
checked whether needed number is in hashmap
if yes returned its index 
if not stored the number



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]                    
"""