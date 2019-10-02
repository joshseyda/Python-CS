# regular function
def square_number(x):
    res = x ** 2
    return res
# lambda function
square = lambda x: x ** 2
# results
print('square_number(4): {}'.format(square_number(4)))
print('square lambda: {}'.format(square(4)))

# >>> square_number(4): 16
# >>> square lambda: 16