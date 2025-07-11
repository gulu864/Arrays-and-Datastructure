def stock(a, a_size):

    profit = 0
    for i in range(1 , a_size):

        if a[i] > a[i-1]:

            profit += a[i] - a[i-1]
    
    return profit

prices = [236,783,967,342,760,120,500]

profit = stock(prices,len(prices))
print("Maximum profit: ",profit)