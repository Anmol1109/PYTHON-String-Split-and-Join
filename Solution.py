def split_and_join(line):
    s = line.split(' ')
    t = '-'.join(s)
    return t
    # write your code here

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result