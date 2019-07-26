def min_of_rev_array(arr):
    if not arr:
        return 0
    a, b = 0, len(arr)-1
    while arr[a] >= arr[b] and not a == b:
        print(a, b)
        mid = (a + b) // 2
        if arr[mid] >= arr[a]:
            a = mid + 1
        elif arr[mid] <= arr[b]:
            b = mid
    return arr[a]


if __name__ == '__main__':
    arr = []
    print(min_of_rev_array(arr))
