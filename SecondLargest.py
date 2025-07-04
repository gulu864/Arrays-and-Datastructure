def sencondlargest(a,arr_size):

    largest = secondlarge = -2147483648

    for i in range(arr_size):

        if (a[i] > largest):

            secondlarge = largest
            largest = a[i]

        elif (a[i] > secondlarge and a[i] != largest):
            secondlarge = a[i]

    print("\nThe second largest nummber in the array is", secondlarge)

a = [1,2,5,3,4,6,9,8,7,3]
arr_size = len(a)
print("Array= ",a)
sencondlargest(a,arr_size)