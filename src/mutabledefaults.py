def incr (increment=1, data=[], newvalues=[]):
    for value in newvalues:
        data.append(value)
    for i in range(len(data)):
        data[i] += increment
    return data

print(incr(newvalues=[1]))
print(incr(newvalues=[1]))
