from typing import List

# O(n) | O(1)
def total_fruit(fruits: List[int]) -> int:
    n = len(fruits)
    i = 0
    result = 0
    map = {}
    for j in range(n):
        map[fruits[j]] = map.get(fruits[j], 0) + 1
        while len(map) > 2:
            map[fruits[i]] -= 1
            if map[fruits[i]] == 0:
                del map[fruits[i]]
            i += 1
        result = max(result, j - i + 1)
    return result