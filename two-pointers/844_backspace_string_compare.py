# c # d #
# write
#     read

# # # 
# write
# read
# write-- if write > 0
# Space O(n + m)
# Time O(n + m)
def backspace_compare(s: str, t: str) -> bool:
    def transform(inputs: list) -> int:
        write, read = 0, 0
        while (read < len(inputs)):
            # [X] inputs[read] == '#' and write > 0
            # When inputs[read] = '#' and write = 0, the else block is entered and # is added
            if inputs[read] == '#':
                if write > 0:
                    write -= 1
            else:
                inputs[write] = inputs[read]
                write += 1
            read += 1
        return write

    first, second = list(s), list(t)
    sizeFirst, sizeSecond = transform(first), transform(second)

    if sizeFirst != sizeSecond:
        return False

    for idx in range(sizeFirst):
        if first[idx] != second[idx]:
            return False

    return True
