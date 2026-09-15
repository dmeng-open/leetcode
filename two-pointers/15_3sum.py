from typing import List

# Time: O(n^2)
# Space: O(1)
def three_sum(inputs: List[int]) -> List[List[int]]:
    inputs.sort() # O(nlog(n))
    triplets = []
    n = len(inputs)
    fixed = 0
    for fixed in range(n - 2): # O(n)
        if fixed > 0 and inputs[fixed] == inputs[fixed - 1]:
            continue
        # 输入值已经排序，如果当前值 > 0，后面的值都 > 0
        if inputs[fixed] > 0:
            break
        left = fixed + 1
        right = n - 1
        while left < right: # O(n)
            sum = inputs[fixed] + inputs[left] + inputs[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                triplets.append([inputs[fixed], inputs[left], inputs[right]]) # O(1)
                while left < right and inputs[left] == inputs[left + 1]:
                    left += 1
                while left < right and inputs[right] == inputs[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        fixed += 1
    return triplets
