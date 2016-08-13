'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0: return False
        dups = set()
        for i in nums:
            if i in dups:
                return True
            else:
                dups.add(i)
        return False

print(Solution().containsDuplicate([1,2,3,4,0]))
