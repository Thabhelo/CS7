def add(x, y):
    return x + y

def curry(func):
    def curried_func(x):
        def inner_func(y):
            return func(x, y)
        return inner_func
    return curried_func

curried_add = curry(add)
add_four = curried_add(4)
result = add_four(6)
print(result)

