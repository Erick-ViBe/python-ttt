def some_decorator(f):
    def function_wrapper():
        print("Before run f")
        f()
        print("After run f")

    return function_wrapper

@some_decorator
def some_function():
    print("Run some_function()")

some_function()

print("***********************************")
print("***********************************")
print("***********************************")

def access_args_Decorator(f: callable):
    def function_wrapper(*args, **kwargs):
        print("Before run f")
        print(args)
        print(kwargs)
        f(*args, **kwargs)
        print("After run f")

    return function_wrapper

@access_args_Decorator
def some_function_2(x):
    print(f"Run some_function(): {x}")

some_function_2(10)
