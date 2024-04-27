def manager_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result == "amir.hm":
            print("Invalid")

    return wrapper
