import functools


def saving_info(initial_func):
    def decorator(func):
        func.__name__ = initial_func.__name__
        func.__doc__ = initial_func.__doc__
        func.__original_func = initial_func
        return func

    # function allows you to save information from original function (__name__ and __doc__)
    # store the original function itself in an attribute
    return decorator


def print_result(func):
    @saving_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
