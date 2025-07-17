def maximum1(a,a_size):

    maxone = 0
    count = 0

    for i in range(1,a_size):

        if a[i] == 0:
            count = 0
        else:
            count += 1
            maxone = max(maxone,count)
    return maxone

a = [1,0,1,0,0,1,0,1,1,1,0,1]
a_size = len(a)
print("array:", a)
print("Maximum consecutive 1's in array:", maximum1(a,a_size))