#  1  0
#  l=>l
#  r
#
#  1  0
#     l
#  r<=r
#  Conclusion: 'left' always land at right of the boundary
#   'right' at left of the boundary

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] == target:
            return center
        elif array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return -1

def general_binary_search(array, isRight):
    left, right = 0, len(array) - 1
    while left <= right:
        center = left + (right - left) / 2
        if isRight(array[center]):
            left = center + 1
        else:
            right = center - 1
    return left

def lower_bound(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] < target:
            left = center + 1
        else:
            right = center - 1
    return left - 1

def upper_bound(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] <= target:
            left = center + 1
        else:
            right = center - 1
    return left

def equal_range(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] < target:
            left = center + 1
        else:
            right = center - 1
    if left >= len(array) or array[left] != target:
        return (-1, -1)
    start = left
    left, right = left, len(array) - 1
    while left <= right:
        center = (left + right) / 2
        if array[center] <= target:
            left = center + 1
        else:
            right = center - 1
    end = right
    return (start, end)
