lst = ['Acer', 'Asus', 'Lenovo', 'HP']
# regular function
def starts_with_a(lst):
    valids = []
 
    for word in lst:
        if word[0].lower() == 'a':
            valids.append(word)
 
    return valids
 
 
# list comprehension
lst_comp = [word for word in lst if word[0].lower() == 'a']
# results
print('starts_with_a: {}'.format(starts_with_a(lst)))
print('list_comprehension: {}'.format(lst_comp))