# 1.01
#   v1_idx
# 1.001
#   v2_idx

# 1.0
#    v1_idx
# 1.0.0.0
#        v2_idx
# O(m + n) | O(1)
def compare_version(v1: str, v2: str) -> int:
    m = len(v1)
    n = len(v2)
    v1_idx = v2_idx = 0
    while v1_idx < m or v2_idx < n:
        # while v1_idx < m and v1[v1_idx] == '0':
        #     v1_idx += 1
        # while v2_idx < n and v2[v2_idx] == '0':
        #     v2_idx += 1
        # 自然就会忽略前导0
        n_v1 = 0
        while v1_idx < m and v1[v1_idx] != '.':
            n_v1 = n_v1 * 10 + (ord(v1[v1_idx]) - ord('0'))
            v1_idx += 1
        n_v2= 0
        while v2_idx < n and v2[v2_idx] != '.':
            n_v2 = n_v2 * 10 + (ord(v2[v2_idx]) - ord('0'))
            v2_idx += 1
        if n_v1 > n_v2:
            return 1
        if n_v1 < n_v2:
            return -1
        v1_idx += 1
        v2_idx += 1
    return 0
