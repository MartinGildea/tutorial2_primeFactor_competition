# primeFactors.py
# import test code
from lab2Test import speedTestFun
# --------------------------------
# primeFactors()
# input:  A positive integer n (e.g. 19162234)
# output: A list of the prime factors of n with multiplicity (e.g. [2, 7, 7, 13, 13, 13, 89])
# method: Divide n by all possible integers in increasing numerical order, which will naturally eliminate
#         non-prime numbers.
# --------------------------------
def primeFactors(n):
    primeList = []    #primeList is the list of all primeFactors of the target number
    primeDivisor = 2  #primeDivisor is a variable that will be added to the list if it can divide the target number without a remainder.
    while primeDivisor * primeDivisor <= n:
        if n % primeDivisor:
            primeDivisor = primeDivisor + 1
        else:
            n = n / primeDivisor
            primeList.append(primeDivisor)
    primeList.append(n)
    return primeList

#testFun(primeFactors)
speedTestFun(primeFactors)
