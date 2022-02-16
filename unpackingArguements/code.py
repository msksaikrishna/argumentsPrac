def multiply(*args):
    total=1
    for i in args:
        total=total*i
    return total

print(multiply(1,2,3))



def apply(*args,operator):
    if operator=='*':
        multiply(*args)
    elif operator=='+':
        sum(args)
    else:
        print('Enter a valid operator')

print(apply(1,2,3,4,5, operator='*'))