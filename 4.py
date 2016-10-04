'''
Problem 4
Largest palindrome product
Find the largest palindrome made from the product of two N-digit numbers
'''
def is_palindrome(num):
    num_str = str(num)
    rev_str = num_str[::-1]
    return num_str == rev_str

def find_largest_palindrome(num):
    palindromes = []
    for i in range(1, num):
        fst = num - i
        for j in range (1, i+1):
            snd = num - j
            if is_palindrome(fst * snd):
                palindromes.append([fst*snd, fst, snd])
    return sorted(palindromes, key=lambda palindrome: palindrome[0], reverse=True).pop(0)

if __name__ == '__main__':
    num = int(input('N= : '))
    if num < 0:
        print('Please input a positive number.')
    result = find_largest_palindrome(10**num)
    print('Answer: {0} = {1} * {2}'.format(result[0], result[1], result[2]))
