'''
Problem 9
Special Pythagorean triplet
Find abc where a + b + c = 1000, a^2 + b^2 = c^2, a < b < c
'''

def find_pythagorean(num):
    a_values = range(1,num-1)
    b_values = range(2, num-1)
    return [(a,b,num-a-b) for a in a_values for b in b_values if a < b and a**2 + b**2 == (num-a-b)**2]

if __name__ == '__main__':
     num = int(input('Enter the sum: '))
     a,b,c = find_pythagorean(num)[0]
     print('Answer: {0}'.format(a*b*c))
