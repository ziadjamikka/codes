def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example sorted array and target value
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

# Call the binary_search function
index = binary_search(arr, target)

# Output the result
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")