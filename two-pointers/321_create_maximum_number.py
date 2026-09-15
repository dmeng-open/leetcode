from typing import List


def max_number(first: List[int], second: List[int], size: int) -> List[int]:
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

    def greater_suffix(first: List[int], second: List[int], first_idx: int=0, second_idx: int=0) -> bool:
        while first_idx < len(first) and second_idx < len(second) and first[first_idx] == second[second_idx]:
            first_idx += 1
            second_idx += 1
        if first_idx == len(first):
            return False
        if second_idx == len(second):
            return True
        return first[first_idx] > second[second_idx]

    def merge_to_max_sequence(first: List[int], second: List[int]) -> List[int]:
        result = []
        first_idx = second_idx = 0

        while first_idx < len(first) or second_idx < len(second):
            if greater_suffix(first, second, first_idx, second_idx):
                result.append(first[first_idx])
                first_idx += 1
            else:
                result.append(second[second_idx])
                second_idx += 1

        return result

    result = []
    for take in range(max(0, size - len(second)), min(size, len(first)) + 1):
        candidate = merge_to_max_sequence(pick_max_subsequence(first, take), pick_max_subsequence(second, size - take))
        if candidate > result:
            result = candidate
    return result
        
