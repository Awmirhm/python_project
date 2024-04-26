import functools
import time

from DataAccessLayer.user_data_access import UserDataAccess

user_data_access = UserDataAccess()


def performance_logger_decorator(*user_clicked):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            present_time = time.ctime()
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time() - start_time
            name_function = function.__name__

            user_data_access.logs(name_function, present_time, end_time)

            print(*user_clicked)

            return result

        return wrapper

    return decorator
