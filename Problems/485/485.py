class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive1 = 0
        tempConsecutive1 = 0

        for num in nums:
            if num == 1:
                tempConsecutive1 += 1
            else:
                if tempConsecutive1 > consecutive1:
                    consecutive1 = tempConsecutive1
                tempConsecutive1 = 0

        if tempConsecutive1 > consecutive1:
            consecutive1 = tempConsecutive1

        return consecutive1
