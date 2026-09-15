def remove_duplicates(nums):
    write = 0
    read = 0
    size = len(nums)

    while read < size:
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]
        read += 1

    return write + 1
