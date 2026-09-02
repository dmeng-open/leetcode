from typing import List


class Solution:
    def pick_max_sequence(self, first: List[int], second: List[int], size: int) -> List[int]:
        def pick_max_subsequence(sequence: List[int], size: int) -> List[int]:
            stack = []
            drop = len(sequence) - size
            for value in sequence:
                while stack and drop > 0 and value > stack[-1]:
                    stack.pop()
                    drop -= 1
                if len(stack) < size:
                    stack.append(value)
                else:
                    drop -= 1
            return stack

        def greater_suffix(first: List[int], second: List[int], i: int=0, j: int=0) -> bool:
            while i < len(first) and j < len(second) and first[i] == second[j]:
                i += 1
                j += 1
            if i == len(first):
                return False
            if j == len(second):
                return True
            return first[i] > second[j]

        def merge_to_max_sequence(first: List[int], second: List[int]) -> List[int]:
            result = []
            i = j = 0

            while i < len(first) or j < len(second):
                if greater_suffix(first, second, i, j):
                    result.append(first[i])
                    i += 1
                else:
                    result.append(second[j])
                    j += 1

            return result

        result = []
        for i in range(max(0, size - len(second)), min(size, len(first)) + 1):
            candidate = merge_to_max_sequence(pick_max_subsequence(first, i), pick_max_subsequence(second, size - i))
            if candidate > result:
                result = candidate
        return result
            