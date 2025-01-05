if __name__ == '__main__':
    s = input()
    is_alnum = False
    for char in s:
        if char.isalnum():
            is_alnum = True
            break
    print(is_alnum)  


    is_alpha = False
    for char in s:
        if char.isalpha():
            is_alpha = True
            break
    print(is_alpha) 

    
    is_digit = False
    for char in s:
        if char.isdigit():
            is_digit = True
            break
    print(is_digit)  

    
    is_lower = False
    for char in s:
        if char.islower():
            is_lower = True
            break
    print(is_lower)  

    
    is_upper = False
    for char in s:
        if char.isupper():
            is_upper = True
            break
    print(is_upper)  
