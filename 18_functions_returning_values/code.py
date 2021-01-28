# def add(x, y):#by default functions return null by default
#     print(x + y)

def add(x, y):#by default functions return null by default
    return(x + y)


add(5, 8)
result = add(5, 8)
print(result)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 3)
print(result)