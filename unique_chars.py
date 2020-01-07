#
# P - go through string and see if there are any repeated letters
# E - "abcde" True
#   - "aabbcc" False
#   - "abca" False
#D  - loops, list, 
#A - Split string into list, compare current index value with the next one
#    if the same false, if no repitions True

def unique_chars(str):
    strList = str.split()
    count = {}
    
    for letter in strList:
        if letter in count:
            return False
        else:
            count[letter] = 1
    return True    
    
    