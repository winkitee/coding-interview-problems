"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeros(self, nums):
        fixed_pos = 0

        for i, num in enumerate(nums):
            if nums[i] != 0:
                if fixed_pos != i:
                    nums[fixed_pos], nums[i] = num, 0
                fixed_pos += 1

        return nums


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
nums = [4, 0, 0, 0, 0, 2, 0, 1, 3, 4, 0, 5]
Solution().moveZeros(nums)
print(nums)

nums = [1, 1, 1, 0]
Solution().moveZeros(nums)
print(nums)
