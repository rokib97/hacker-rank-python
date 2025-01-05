def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string) + i]:
            count += 1
        
    print(count) 
        
string = 'ABCDCDC'    
sub_string = 'CDC'
count_substring(string, sub_string)

    
