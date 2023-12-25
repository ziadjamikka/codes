def linear_search(arr , target):
    for element , index in enumerate(arr):
        if element == target:
            return index
    return -1
index = linear_search(arr , target)
