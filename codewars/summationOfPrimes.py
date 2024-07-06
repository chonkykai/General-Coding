def summationOfPrimes(primes):
    sum = 2

    for num in range(2, primes + 1):

        i = 2
        
        for i in range(2, num):
            if (int(num % i) == 0):
                i = num
                break

        #If the number is prime then add it.
        if i is not num:
            sum += num
    return sum