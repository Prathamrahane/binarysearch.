def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
     if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  
numbers = [1, 4, 10, 26, 33, 36, 42, 75, 91]
target_number = 33
result = binary_search(numbers, target_number)
if result != -1:
    print("Target found at index", result)
else:
    print("Target not found")
