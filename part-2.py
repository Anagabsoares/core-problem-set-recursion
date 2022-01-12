# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(arr, target):
    if not arr:
        return False
    elif arr[0] == target:
        return True
        
    print(arr[1:])
  
    return search(arr[1:], target)
            
            
         


# is_palindrome

def  is_palindrome(word):
    
    reversed_word = reverse(word)

    if word == reversed_word:
        return True
    else:
        return False



def reverse(word):
    if len(word) <= 1:
        return word
    
    first_char = word[:1]
    remaining_chars = word[1:]
    return reverse(remaining_chars) + first_char 

# digit_match


def digit_match(int1, int2):

    if int1 <10 or int2 <10:
        if int1 % 10 == int2 %10 :
            return 1
        else:
            return 0
    if int1 % 10 == int2%10:
        return 1 + digit_match(int1//10, int2//10)
        
    return digit_match(int1//10, int2//10)


