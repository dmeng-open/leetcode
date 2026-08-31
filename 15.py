from typing import List

class Solution:
    def threeSum(self, inputs: List[int]) -> List[List[int]]:
        inputs.sort()
        triplets = []
        n = len(inputs)
        i = 0
        for i in range(n - 2):
            if i > 0 and inputs[i] == inputs[i - 1]:
                continue
            # 输入值已经排序，如果当前值 > 0，后面的值都 > 0
            if inputs[i] > 0:
                break
            j = i + 1
            k = n - 1
            while j < k:
                sum = inputs[i] + inputs[j] + inputs[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    triplets.append([inputs[i], inputs[j], inputs[k]])
                    while j < k and inputs[j] == inputs[j + 1]:
                        j += 1
                    while j < k and inputs[k] == inputs[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return triplets