def linearsearch(arr, val):
    count = 0
    for index in arr:
        if arr[count] == val:
            return count
        count+=1
    return -1

arr1 = ["hey", "ho", "uncle"]
print(linearsearch(arr1, "uncle"))