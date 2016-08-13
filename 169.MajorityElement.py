class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > n:
                return i

print(Solution().majorityElement([1,2,2,2,2,3,3,3,3,3,3,3]))
