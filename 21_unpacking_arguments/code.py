def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1,3,5,6, operator='*'))

# test = multiply(1, 3, 5)

# print(test)

def add(x, y):
    return x + y

# nums = [3, 5]
# add(*nums)#the number of values in the list must be equal to the number of parameters

nums = {"x": 15, "y": 25}
print(add(**nums))