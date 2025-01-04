nested_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])
lowest = float("inf")
second_lowest = float("inf")
for _, score in nested_list: 
    if score < lowest:
        second_lowest = lowest
        lowest = score
    elif lowest < score < second_lowest:
        second_lowest = score
second_lowest_names = []
for name, score in nested_list:
    if score == second_lowest:
        second_lowest_names.append(name)
second_lowest_names.sort()
for name in second_lowest_names:
    print(name)
