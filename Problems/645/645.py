class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            if (nums[i] == nums[i + 1]):
                return [nums[i], nums[i] + 1]
