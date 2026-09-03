# 1.01
#   i
# 1.001
#   j

# 1.0
#    i
# 1.0.0.0
#        j
# O(m + n) | O(1)
def compare(v1: str, v2: str) -> int:
    m = len(v1)
    n = len(v2)
    i = j = 0
    while i < m or j < n:
        # while i < m and v1[i] == '0':
        #     i += 1
        # while j < n and v2[j] == '0':
        #     j += 1
        # 自然就会忽略前导0
        n_v1 = 0
        while i < m and v1[i] != '.':
            n_v1 = n_v1 * 10 + (ord(v1[i]) - ord('0'))
            i += 1
        n_v2= 0
        while j < n and v2[j] != '.':
            n_v2 = n_v2 * 10 + (ord(v2[j]) - ord('0'))
            j += 1
        if n_v1 > n_v2:
            return 1
        if n_v1 < n_v2:
            return -1
        i += 1
        j += 1
    return 0