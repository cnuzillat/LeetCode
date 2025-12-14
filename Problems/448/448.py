class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        disappearedNumsLst = []

        for i in range(1, len(nums) + 1):
            if i not in setNums:
                disappearedNumsLst.append(i)

        return disappearedNumsLst
