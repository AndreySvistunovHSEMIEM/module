def binary_search(arr: list, target) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear_search(arr: list, target) -> int:
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
