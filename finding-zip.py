# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text =  "We believe university-level zip education can be both high quality and low cost. Using the economics of the Internet, we've connected some of the greatest teachers to hundreds of thousands of students all over the world."
text_2 = text.lower()

# ENTER CODE BELOW HERE
def zipper(input):
    zip = input.find('zip')
    zip_1 = text_2[zip+1:]
    zip_2 = zip_1.find('zip') 
    if zip_2 == -1: 
        print zip_2
    else:
        sorted = zip + zip_2 + 1
        print sorted

zipper(text)


# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function












