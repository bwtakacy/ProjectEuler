'''
Problem 5
Smallest multiple
Find the smallest positive number which is evenly divisible by all of the numbers from 1 to N
'''
PRIMES=[2,3,5,7,11,13,17,19]

def find_max_multiple(num, N):
    for i in range(1, N//num+1):
        if num**i > N:
            return num**(i-1)
    return num

if __name__ == '__main__':
    num = int(input('Enter the number: '))
    if num < 0:
        print('Please input a positive number.')
    result = 1
    for p in PRIMES:
       if p > num:
           break
       print('{0} : {1}'.format(p, find_max_multiple(p, num)))
       result *= find_max_multiple(p, num)
    print('Answer: {0}'.format(result))
