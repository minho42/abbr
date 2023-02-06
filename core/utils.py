import time
from functools import wraps
from typing import List, Union

from django.conf import settings
from django.http import Http404

def timeit(func):
    @wraps(func)
    def closure(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("<%s> took %0.3fs." % (func.__name__, te - ts))
        return result

    return closure


def get_all_fields(model) -> List[str]:
    # print('---------------------------')
    # pprint.pprint(model._meta.__dict__)
    # print('---------------------------')

    r = []
    try:
        # r = [f.name for f in model._meta.__dict__["local_fields"]]
        r = [f.name for f in model._meta.local_fields]
    except KeyError:
        pass
    else:
        pass
    return r


def get_all_fields_excluding(model, exclude_list: List[str]) -> List[str]:
    if type(exclude_list) is not list:
        raise TypeError("exclude_list must be list")

    include_list = get_all_fields(model)

    for i in include_list:
        for e in exclude_list:
            e = e.strip()
            if e in include_list:
                include_list.remove(e)

    return include_list


def superuser_check(user: object) -> Union[bool, object]:
    """To be used as parameter for @user_passes_test
    View is only available for superuser otherwise raise 404"""
    if user.is_superuser:
        return True
    raise Http404()


def staff_check(user: object) -> Union[bool, object]:
    """To be used as parameter for @user_passes_test
    View is only available for staff otherwise raise 404"""
    if user.is_staff:
        return True
    raise Http404()
