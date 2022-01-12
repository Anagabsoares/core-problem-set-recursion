# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

# factorial - number * itself -1 until it reaches 1
# base case n -1 =1
# recursive case number * itself - 1


def factorial(n):
    if(n) <0:
        raise ValueError()
        
    if (n) ==0:
        return 1
    
    return  n * factorial(n-1)


# reverse
def reverse(word):
    
    if len(word) <= 1:
        return word
    
    first_char = word[:1]
    remaining_chars = word[1:]
    return reverse(remaining_chars) + first_char    
    
    
    

print(reverse('hello'))


# bunny
def bunny(num):
    if num == 0:
        return 0
    
    return bunny(num-1) +2
    
 
    


# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        print(parens[:1])
        return False
    else:
        return is_nested_parens(parens[1:-1])
    
