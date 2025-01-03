n = 5
lst = [2, 3, 6, 6, 5]

max_val = float("-inf")
second_max = float("-inf")

for num in lst:
    if num > max_val:
        second_max = max_val  
        max_val = num        
    elif num > second_max and num != max_val:
        second_max = num 

print(max_val, second_max)

