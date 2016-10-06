'''
Problem 7
10001st prime
What is the 10001st prime number
'''
from math import sqrt
MAX=200000
def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    N = int(input('Enter the number: '))
    primes = [x for x in  range(1, MAX) if is_prime(x) ]
    print('Answer: {0}'.format(primes[N]))
