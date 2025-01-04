query_name = 'alpha'

student_dict = {
     'beta' : [30,50,70],
     'alpha' : [52, 56, 60]
}

for key,value in student_dict.items():
    if query_name in key:
        avg = sum(value)/len(value)
        # print(round(avg, 2))
        print(f"{avg:.2f}")
        # print("{:.2f}".format(avg))
        