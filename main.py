def binary_search(arr , target):
    left , right = 0 , len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target :
            left = mid +1
        else: 
            right = mid -1
    return -1
arr = [1,5,7,8,1,4,5,8,7]
target = 7
index = binary_search(arr , target)
if index != -1:
    print(f"element {target} found at {index}")
else:
    print(f"element {target} not found")