def urlparse_(url):
    try: # for Python 3
        from urllib.parse import urlparse

    return urlparse(url)