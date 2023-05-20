def my_max(*args) -> str:
    maximum = args[0]
    for arg in args:
        if arg > maximum:
            maximum = arg

    return maximum

def my_min(*args) -> str:

    result = args[0]
    for arg in args[1:]:
        if arg < result:
            result = arg
    return result