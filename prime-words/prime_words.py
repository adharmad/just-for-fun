# Prime words

import sys, string, math

ALL_SYMBOLS = string.digits + string.ascii_uppercase
cache = {}

def getSymbolValue(s):
	"""
	Get the value for the symbol.
	The symbols 0 to 9 return the same number. However symbols A to Z
	will return numbers from 10 to 35
	"""
	return ALL_SYMBOLS.find(s)

def getBasePower(base, exp):
	"""
	Gets the powers of the base in a slightly efficient way by caching
	previously calculated powers.
	Keep a cache with a tuple of (base, exp) as the key and base^exp
	as the value
	[This would be better if there was a module for memoization]
	"""
	if (base, exp) not in cache.keys():
		cache[(base,exp)] = int(math.pow(base, exp))
	return cache[(base,exp)]

def getDecimalValue(w):
	"""
	String w will be a word like TREE or FROG. This function will 
	calculate the decimal value of this "word" by assuming that it 
	is a number in base 36 like:
		'T' * 36^3 + 'R' * 36^2 + 'E' * 36 + 'E'
	"""
	decValue = 0

	for i in range(len(w)):
		decValue = decValue + (getSymbolValue(w[i]) * getBasePower(36, i))

	return decValue

def isPrime(n):
    """
    Checks if the number is prime
    """
    # Return false if numbers are less than 2
    if n < 2:
        return False

    # 2 is smallest prime
    if n == 2:
        return True

    # All even numbers are not prime
    if not n & 1:
        return False

    # Now start at 3, go upto the square root of the number and check
    # for divisibility. Do this in steps of two so that we consider
    # only odd numbers
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False

    # number is prime
    return True

if __name__ == '__main__':
    w = sys.argv[1]
    n = getDecimalValue(w)
    
    if isPrime(n):
        print (w, " is prime")
    else:
        print (w, " is not prime")
