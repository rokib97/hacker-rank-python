import textwrap

mystr = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

# result = textwrap.wrap(mystr, width=20)
result = textwrap.fill(mystr, width=4)
print(result)