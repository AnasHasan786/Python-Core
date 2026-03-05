def check_datatype(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("Invalid datatype!!")

        return inner_wrapper

    return outer_wrapper


@check_datatype(int)
def square(num):
    print(num**2)


@check_datatype(str)
def greet(name):
    print(name)


square(4)
greet("Ajay")
