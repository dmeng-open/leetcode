# T: O(m + n)
# S: O(1)
# internationalization
#                     s_idx
# i19
#    abbr_idx
# n = 1
# n = 10 * n + abbr[abbr_idx]
#   = 10 * 1 + 2 = 12
def valid_word_abbreviation(s: str, abbr: str) -> bool:
    s_idx = abbr_idx = 0
    while abbr_idx < len(abbr):
        if abbr[abbr_idx].isdigit():
            if abbr[abbr_idx] == '0':
                return False
            else:
                n = 0
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    n = 10 * n + int(abbr[abbr_idx])
                    abbr_idx += 1

                s_idx += n

                # Skip too far
                # s = word
                # abbr = 5d
                if s_idx > len(s):
                    return False

                # For a valid abbr, if now s_idx = len(s), then abbr_idx is also len(abbr) and thus no next loop
        else:
            # Need a char, none left
            # s = word
            # abbr = 4d
            if s_idx >= len(s) or s[s_idx] != abbr[abbr_idx]:
                return False
            
            s_idx += 1
            abbr_idx += 1
    return s_idx == len(s) # Didn't consume all of s
