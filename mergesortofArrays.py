# example of merge sort in Python
# merge function take two intervals
# first from start to mid
# second from mid+1, to end
# and merge them in sorted order
def merge(arr, start, mid, end):
    # create a temp array
    temp = [0] * (end - start + 1)
    # crawlers for both intervals and for temp
    i = start
    j = mid + 1
    k = 0
    # traverse both lists and in each iteration add smaller of both elements in temp
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    # add elements left in the first interval if there are any
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    # add elements left in the second interval if there are any
    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1
    # copy temp to original interval
    for i in range(start, end + 1):
        arr[i] = temp[i - start]


# arr is an array of integer type
# start and end are the starting and ending index of current interval of Arr
def mergeSort(arr, start, end):
    if start < end:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        mid = start + (end - start) // 2

        # Sort first and second halves
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7,
       3, 5, 4, 3, 2, 2, 2,
       4, 5, 3, 5, 4, 3, 3,
       3, 4, 1, 3, 3, 65, 3,
       3, 3, 3214, 34, 4, 4,
       43, ]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
