def myfilter(comparator, iterator):
    res = tuple()
    for elem in iterator:
        if comparator(elem):
            res += (elem, )
    return res


def positive(x):
    return True if x > 0 else False


nums = tuple(range(-7, 8))
print(nums, end='\n\n')
nums_pos = myfilter(positive, nums)
print(nums_pos, end='\n\n')
