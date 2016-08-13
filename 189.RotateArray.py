'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def oneRightRotate(nums):
            temp = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp

        print (nums)
        while k:
            oneRightRotate(nums)
            k -= 1
        print (nums)

    def rotateFaster(self, nums, k):
        l = len(nums)
        if k >= l: k = k % l
        temp = nums[l-k:l]
        for i in range(l-1, k - 1, -1):
            nums[i] = nums[i - k]
        nums[0:k] = temp
        print (nums)
    
    def rotateWithReverse(self, nums, k):

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        k, end = k % len(nums), len(nums) - 1
        reverse(nums, 0, end - k)
        reverse(nums, end - k + 1, end)
        reverse(nums, 0, end)
        print(nums)

Solution().rotateWithReverse([1,2,3,4,5,6,7,8],9)
