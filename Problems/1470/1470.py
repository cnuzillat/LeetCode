class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        firstHalfLst = nums[0:len(nums)//2]
        secondHalfLst = nums[len(nums)//2:len(nums)]

        resultsLst = []

        for i in range (len(firstHalfLst)):
            resultsLst.append(firstHalfLst[i])
            resultsLst.append(secondHalfLst[i])

        return resultsLst
