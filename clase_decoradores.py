def prints(func, show_line=False):
    def decorated_func(*args, **kwargs):
        print(func.__name__)
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
        if show_line:
            print('=' * 20)
        return result

    return decorated_func


def triple(a, b, c):
    return a * b * c

@prints
def multiply(a, b):
    return a * b


def sums(a, b):
    return a + b

sums = prints(sums, show_line=True)

a = 1
b = 7

multiply(a, b)
sums(a, b)

multiply(a=5, b=8)
multiply(5, b=8)
