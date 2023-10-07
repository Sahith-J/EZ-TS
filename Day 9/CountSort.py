#Count Sort is mostly for duplicate elements
# Bubble , Insertion are stable
# Selection is unstable
def count_sort(arr):
    max1 = max(arr)
    min1 = min(arr)
    range1 = max1 - min1 + 1
    count = [0] * range1
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min1] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min1] - 1] = arr[i]
        count[arr[i] - min1] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
count_sort(arr)
print(arr)
