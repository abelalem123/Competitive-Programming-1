def swap_case(s):
    result=[]
    for l in s:
        if l.isupper():
            result.append(l.lower())
        elif l.islower():
            result.append(l.upper())
        else:
            result.append(l)
    return ''.join(result)

if __name__ == '__main__':
