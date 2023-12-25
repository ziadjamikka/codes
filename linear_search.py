def linear_search(arr , target):
    for index , element in enumerate(arr):
     if element ==target:
        return index
    return -1
# example array and target value :
arr = [4,2,7,1,9,3]
target = 7
# call the linear_search:
index = linear_search(arr , target)
# output the result :
if index != -1:
   print(f"element {target} found at  index {index}")
else:
   print(f"element {target} not found at in the array")
   