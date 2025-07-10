def Revergroup(a ,arr_size, n):

    temp = 0

    while(temp<arr_size):

        start = temp
        end = min(temp + n - 1,arr_size - 1)

        while (start < end):

            a[start], a[end] = a[start], a[end]
            start +=1
            end -= 1

        temp+= n
    return a

a = [1,2,3,4,5,6,7,8,9,10]

n = 2
arr_size = len(a)
b = Revergroup(a,arr_size,n)

for i in range(0,arr_size):
    print(b[i],end=" ")