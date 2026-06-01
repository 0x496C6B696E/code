class Solution1:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                total += cost[i]
        return total


class Solution2:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        del cost[2::3]
        return sum(cost)