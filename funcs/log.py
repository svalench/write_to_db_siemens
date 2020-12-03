import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s -  %(levelname)s - %(message)s')

info_log = logging.FileHandler('info.log')
info_log.setLevel(logging.INFO)
info_log.setFormatter(formatter)

logger.addHandler(info_log)





def decor_log(func):
    def wrapper(*args,**kwargs):
        logger.info(func.__doc__)
        return func(*args, **kwargs)
    return wrapper

def decor_raise(func):
    def wrapper(*args,**kwargs):
        try:
             return func(*args, **kwargs)
        except Exception as er:
            logger.error(f'Error value in {func.__name__} with error {er}',  exc_info=True)

    return wrapper

def class_decorator_log(cls):
    for name, method in cls.__dict__.iteritems():
        if not name.startswith('_'):
            setattr(cls, name, decor_log(method))
    return cls