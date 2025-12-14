class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        resultLst = []

        for i in range(0, len(nums)):
            greaterThanCount = 0
            for j in range(0, len(nums)):
                if (nums[i] > nums[j]):
                    greaterThanCount += 1
            resultLst.append(greaterThanCount)
        
        return resultLst
