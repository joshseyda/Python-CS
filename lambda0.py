# regular function
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
 
 
# lambda function
even = lambda x: x % 2 == 0
# results
print('is_even(4): {}'.format(is_even(4)))
print('is_even(3): {}'.format(is_even(3)))
print('even(4): {}'.format(even(4)))
print('even(3): {}'.format(even(3)))