import functools
import time
from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer.get_user import GetUser

user_data_access = UserDataAccess()


def performance_logger_decorator():
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            present_time = time.ctime()
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time() - start_time
            name_function = function.__name__
            if GetUser.current_user:
                user_data_access.logs(name_function, present_time, end_time,GetUser.current_user)

            return result

        return wrapper

    return decorator
