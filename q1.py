def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    length = len(s)
    max_len = 0 
    result = "" 
    
    for i in range(length):
        x, y = i, i 
       
        while x >= 0 and y < length and s[x] == s[y]: 
            
            if (y - x + 1) > max_len:
                max_len = y - x + 1
                result = s[x:y+1]
            x -= 1
            y += 1
            
        x, y = i, i + 1 
     
        while x >= 0 and y < length and s[x] == s[y]: 
            
            if (y - x + 1) > max_len:
                max_len = y - x + 1
                result = s[x:y+1]
            x -= 1
            y += 1

    if max_len < 2:
        return ""  

    return result
