#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return_value = fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
    return return_value