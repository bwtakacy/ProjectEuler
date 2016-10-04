'''
Problem 2
Even Fibonacci numbers
Find the sum of the even value terms of Fibonacci numbers
'''
def fibo(n):
    if n == 1:
        return [1]
    a = 1
    b = 1
    series = [b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
        if b > n:
            break
    return series

def sum_even_fibo(num):
    even_fibo_nums = [ x for x in fibo(num) if x % 2 == 0]
    print('Answer: {0}'.format(sum(even_fibo_nums)))

if __name__ == '__main__':
    num = int(input('Enter the number: '))
    if num < 0:
        print('Please input a positive number.')
    sum_even_fibo(num)
