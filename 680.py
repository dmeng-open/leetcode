# T: O(n)
# S: O(1)
class Solution:
    # a b c a
    #  i
    #     j

    # a b x c a
    #   i
    #        j

    # a b c c a
    #   i
    #     j
    def valid(self, s: str) -> bool:
        def check(i, j) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if (s[i] == s[j]):
                i += 1
                j -= 1
            else:
                return check(i + 1, j) or check(i, j - 1)
        return True
                
        
