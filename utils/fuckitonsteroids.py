import fuckit
def fuckitonsteroids(err_message):
    def decorator(helper):
        def wrapper(*args, **kwargs):
            helper_result = fuckit(helper)(*args, **kwargs)
            if helper_result:
                return helper_result
            raise ValueError(err_message)
        return wrapper
    return decorator
