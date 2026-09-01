# T: O(m + n)
# S: O(1)
class Solution:
    # internationalization
    #                     i
    # i19
    #    j
    # n = 1
    # n = 10 * n + abbr[j]
    #   = 10 * 1 + 2 = 12
    def valid(self, s: str, abbr: str) -> bool:
        i = j = 0
        while j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                else:
                    n = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        n = 10 * n + int(abbr[j])
                        j += 1

                    i += n

                    # Skip too far
                    # s = word
                    # abbr = 5d
                    if i > len(s):
                        return False
            else:
                # Need a char, none left
                # s = word
                # abbr = 4d
                if i >= len(s) or s[i] != abbr[j]:
                    return False
                
                i += 1
                j += 1
        return i == len(s) # Didn't consume all of s