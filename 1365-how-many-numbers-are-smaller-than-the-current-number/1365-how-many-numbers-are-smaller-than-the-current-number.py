class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))
        d = {}

        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i

        ret = []

        for i in nums:
            ret.append(d[i])

        return ret






"""
The question goes as we have to return all the numbers which are less than each number in nums whether they are similar or not wont matter

so firstly we will sort all the nums 
then we will implement the enumerate way to approach problem
creating index with number pairs 
now we will create a list
now after all this going again to the nums and matching the value let say for [8,1,2,2,3]
we are matching 8 with the index of 8 in our hashmap d
8 comes in position at the index 4 as per the d
so number of numbers which are less than 8 are actual 4. (quite obivious that in a sorted list all the numbers before 8 are smaller that it and count of those numbers are none other but the index of the number)



BRUTEFORCE:

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)

        return ans

"""