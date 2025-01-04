n = int(input(""))
my_list = []
for i in range(n):
    latest_command = input().split()
    if latest_command[0] == 'insert':
        my_list.insert(int(latest_command[1]), int(latest_command[2]))
    elif latest_command[0] == 'remove':
        my_list.remove(int(latest_command[1]))
    elif latest_command[0] == 'append':
        my_list.append(int(latest_command[1]))
    elif latest_command[0] == 'sort':
        my_list.sort()
    elif latest_command[0] == 'pop':
        my_list.pop()
    elif latest_command[0] == 'reverse':
        my_list.reverse()
    else:
        print(my_list)