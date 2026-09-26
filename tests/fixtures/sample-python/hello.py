def used_function():
    return "hello"


def unused_function():
    return "this is dead code"


result = used_function()
print(result)
