'''
Problem 3
Largest prime factor
Find the largest prime factor of the given number
'''
def prime_decomp(num):
    i = 2
    decomp = []
    while i * i <= num:
        while num % i == 0:
            num /= i
            decomp.append(i)
        i += 1
    if num > 1:
        decomp.append(int(num))
    print(decomp)
    return decomp

if __name__ == '__main__':
    num = int(input('Enter the number: '))
    if num < 0:
        print('Please input a positive number.')
    ans = prime_decomp(num)
    print('Answer: {0}'.format(ans[-1]))
