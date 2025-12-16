class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []

        numsHash = {}

        for num in nums:
            if num in numsHash:
                result.append(num)
            else:
                numsHash[num] = 1

        for i in range (1, len(nums) + 1):
            if i not in numsHash:
                result.append(i)

        return result
