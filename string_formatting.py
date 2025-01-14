def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        print(f"{i}".rjust(width),
              "{0:o}".format(i).rjust(width),
              "{0:X}".format(i).rjust(width),
              "{0:b}".format(i).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
