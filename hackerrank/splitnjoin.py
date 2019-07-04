def split_and_join(line):
    b = line.split(" ")
    b=  "-".join(b)
    return b
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
