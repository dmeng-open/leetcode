from typing import List


class Solution:
    def intervalIntersections(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        n = len(firstList)
        m = len(secondList)
        while i < n and j < m:
            # 1. 计算当前两个区间的交集
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            # 2. 判断是否形成了交集，略过或者加入结果
            # [1, 3] 和 [5, 7] start = 5 end = 3 没有交集
            if start <= end:
                result.append([start, end])
            # 3. 移动 end 靠前的指针
            # [[2, 3], [3, 4], [5, 6]] 和 [[1, 20]]
            # end 较小的区间已经不可能和另一个列表里后面的区间形成交集
            # 因为同列表中的区间是 disjoint
            # end 较大的区间还有可能和另一个列表中后面区间形成交集
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return result