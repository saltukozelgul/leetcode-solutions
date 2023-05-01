import itertools
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        difference = 10000
        endPointer = len(nums) - 1
        returnValue = 0
        for x in range(len(nums)):
            a = x+1
            b = endPointer
            while a < b:
                summ = nums[x] + nums[a] + nums[b]
                absolute = abs(summ - target)
                if (absolute< difference):
                    difference = absolute
                    returnValue = summ
                if summ == target:
                    return summ
                elif summ < target:
                    a += 1
                else:
                    b -= 1
        return returnValue 
        

