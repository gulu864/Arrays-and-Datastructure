def push0(a,a_size):

    zero = 0
    nonzero = 0

    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero += 1
        nonzero += 1

a = [1,0,9,0,4,3,5,0,0,39,0,2,3,0,0,1,2,5]
a_size = len(a)
print("Array:", a)
push0(a,a_size)
print("Array after pusing all 0's to the end:", a)