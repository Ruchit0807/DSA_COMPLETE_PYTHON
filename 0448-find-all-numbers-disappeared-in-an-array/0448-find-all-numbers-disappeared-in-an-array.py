class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        a = []
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                a.append(i)
    
        return a

"""
This problem is we have to calculate misssing numbers from nums where n = len(nums).
therefore [1,1] got output as missing 2 because n = 2 (1 and 1) so our required range should be from [1,2].
this can be solved as whenever we see duplicated we try to use sets 
and by defining i which is from [1,n] and checking for all elements in the sets.

"""