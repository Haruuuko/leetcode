'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i

        return False

print(Solution().containsNearbyDuplicate([4, 0, 4, 6, 9], 2))
