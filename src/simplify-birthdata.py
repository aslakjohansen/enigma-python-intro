values = []

with open('2020118194823303242491FODDAG77873904000.csv', encoding='cp1252') as fo:
    ilines = fo.readlines()

for line in ilines:
    elements = line.strip().split(';')
    
    if len(elements)!=3: continue
    if elements[2]=='': continue
    if elements[2]=='..': continue
    if elements[2][0]=='"': continue
    
    values.append(int(elements[2]))

print('Fount %d values'%len(values))

with open('dkbirths2019.csv', 'w') as fo:
    fo.writelines(map(lambda i: '%d,%d\n'%(i, values[i]), range(len(values))))
