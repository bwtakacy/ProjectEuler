'''
Problem 6
Sum square difference
Find the difference between the sum of the squares and the square of the sum
'''
def calc_sum_of_squares(num):
    result = 0
    for i in range(1, num+1):
        result += i**2
    return result

def calc_square_of_sum(num):
    result = 0
    for i in range(1, num+1):
        result += i
    return result**2

if __name__ == '__main__':
    num = int(input('N= : '))
    if num < 0:
        print('Please input a positive number.')
    diff = calc_square_of_sum(num) - calc_sum_of_squares(num)
    print('Answer: {0}'.format(diff))
