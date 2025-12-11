class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rowMax = [0] * (n + 1)
        rowMin = [n + 1] * (n + 1)
        columnMax = [0] * (n + 1)
        columnMin = [n + 1] * (n + 1)

        for x, y in buildings:
            rowMax[y] = max(rowMax[y], x)
            rowMin[y] = min(rowMin[y], x)
            columnMax[x] = max(columnMax[x], y)
            columnMin[x] = min(columnMin[x], y)

        ans = 0

        for x, y in buildings:
            if rowMin[y] < x < rowMax[y] and columnMin[x] < y < columnMax[x]:
                ans += 1

        return ans
