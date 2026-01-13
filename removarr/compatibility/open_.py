def open_(name, mode='r', **kwargs):
    try: # for Python 3
        return open(name, **kwargs)