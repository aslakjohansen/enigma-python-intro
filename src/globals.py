a = 42
b = 56

def fun (value):
    global b
    
    a = value
    b = value
    print(a, b)

fun(-1)
print(a, b)
