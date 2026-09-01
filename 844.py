class Solution:
    # c # d #
    # i
    #     j

    # # # 
    # i
    # j
    # i-- if i > 0
    # Space O(n + m)
    # Time O(n + m)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def transform(inputs: list) -> int:
            w, r = 0, 0
            while (r < len(inputs)):
                # [X] inputs[j] == '#' and i > 0
                # When inputs[j] = '#' and i = 0, the else block is entered and # is added
                if inputs[r] == '#':
                    if w > 0:
                        w -= 1
                else:
                    inputs[w] = inputs[r]
                    w += 1
                r += 1
            return w

        first, second = list(s), list(t)
        sizeFirst, sizeSecond = transform(first), transform(second)

        if sizeFirst != sizeSecond:
            return False

        for i in range(sizeFirst):
            if first[i] != second[i]:
                return False

        return True