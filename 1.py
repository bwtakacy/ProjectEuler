'''
Problem 1
Multiples of 3 and 5
Find the sum of all the multiples of 3 or 5 below given number
'''
def sum_multiples(num):
    multiples = [ x for x in range(1,num) if x % 3 == 0 or x % 5 == 0]
    print('Answer: {0}'.format(sum(multiples)))

if __name__ == '__main__':
    num = int(input('Enter the number: '))
    if num < 0:
        print('Please input a positive number.')
    sum_multiples(num)
