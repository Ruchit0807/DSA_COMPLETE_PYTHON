#BEST APPROACH

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums)) #Since set stores only unique values

#BRUTEFORCE APPROACH

# class Solution:
#     def containsDuplicate(self, nums):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
