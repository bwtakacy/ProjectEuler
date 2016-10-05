'''
Problem 5
Smallest multiple
Find the smallest positive number which is evenly divisible by all of the number from 1 to 20
'''
MAX = 100000000

def filter_divisible(lst, num):
    return [x for x in lst if x % num == 0]

def smallest_multiple(N):
    lst = range(1, MAX)
    for i in range(2, N+1):
       lst = filter_divisible(lst, i) 
    return lst

if __name__ == '__main__':
    num = int(input('N= : '))
    if num < 0:
        print('Please input a positive number.')
    print('Answer; {0}'.format(smallest_multiple(num)[0]))
