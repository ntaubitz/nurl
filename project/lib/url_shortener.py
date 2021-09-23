import random


# This is a class, but the more pythonic way would be to just import the method.
# There is a class because I thought I would do much more with this concept, like
# pre generating nurls in a table.
class UrlShortener(object):
    base_url = "https://nur.ly/"

    @staticmethod
    def shorten_url():
        # 97 to 122
        # We could use just lower case characters and not randomize it
        # However this would be very predictable.
        # Ideally we could generate all possibilities in a store and then monitor them
        # If a nurl wasn't used for N period of time we could "recycle" it.
        index = random.randint(97, 122)
        key = ""
        # If I had to ship this, I would log the index and have a monitor with a threshold.
        # If we started getting to many collisions, then it would need to change
        while 1:
            test_char = chr(index)
            yield "{url}{key}{test_char}".format(url=UrlShortener.base_url, key=key, test_char=test_char)
            index = index + 1
            if index >= 122:
                key += test_char
                index = random.randint(97, 122)


