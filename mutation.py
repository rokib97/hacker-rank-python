string = 'abracadabra'
position = 5
character = 'k'

string_arr = list(string)
for index, _ in enumerate(string_arr):
    if index == position:
        string_arr[index] = character
print("".join(string_arr))
