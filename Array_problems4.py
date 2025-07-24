def Equilibrium_number(a):

    LSsum = 0
    RSsum = 0
    a_size = len(a)

    for i in range(a_size):
         
        LSsum = 0
        RSsum = 0

        for x in range(i):

            LSsum += a[x]
        
        for x in range(i+1,a_size):

            RSsum += a[x]

        if LSsum == RSsum:

            return a[i]
    return -1

a = [1,6,-3,5,9,3,4,4,-2]
print("Array:",a)
print("Equilibrium number in array:",Equilibrium_number(a))