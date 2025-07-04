#Mean = maximum#
def arrayMean(arr,arr_size):

    total_sum = 0
    for i in range(0,arr_size):
        total_sum += arr[i]
    return float(total_sum/arr_size)

#Median = middle#
def arrayMedian(arr,arr_size):

    sorted(arr)

    if arr_size % 2 != 0:
        return float(arr[int(arr_size/2)])
    return float((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2.0)

arr = [1,4,5,2,3,4,1,3,5]
arr_size = len(arr)

print("Array= ",arr)
print("Mean array: ",arrayMean(arr,arr_size))
print("Median array: ",arrayMedian(arr,arr_size))