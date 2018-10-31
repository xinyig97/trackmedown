inp = input('giveme your file:')
fhand = open(inp)
for line in fhand:
    if 'Invalid' in line:
        line.rstrip()
        pos = line.find('from ')
        user = line[pos+5:]
        print(user)
        
