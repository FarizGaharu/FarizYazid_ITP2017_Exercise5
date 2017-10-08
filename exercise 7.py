def log(original_func):
    def new_func(*args, **kwargs):
        with open("log.txt", "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_func.__name__, args, kwargs))

        return original_func(*args, **kwargs)

    return new_func

@log
def add(a, b):
    return a + b

print(add(4.5,9))
print(log(add(4.5,9)))
