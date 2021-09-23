from project.model.nurl import NUrl
from project.lib.url_shortener import UrlShortener


class NUrlRepository(object):
    __instance = None

    @staticmethod
    def get_instance():
        if NUrlRepository.__instance is None:
            NUrlRepository()
        return NUrlRepository.__instance

    @property
    def shortened(self):
        return self.__shortened

    @property
    def originals(self):
        return self.__originals

    def __init__(self):
        if NUrlRepository.__instance is not None:
            raise Exception("There can be only one ring")
        else:
            NUrlRepository.__instance = self
        # This would actually use SQL queries instead of just holding them in memory
        self.__shortened = {}
        self.__originals = {}

    def get_or_create(self, url):
        if url not in self.__originals:
            # I would have a table of generated urls to be consumed here.
            # If there wasn't any due to a job not running to generate short urls,
            # then that same logic could be called to generate one on demand
            shortened_url = ""
            for surl in UrlShortener.shorten_url():
                # SELECT count(id) FROM nurls where shortened_url = {surl}
                if surl not in self.__shortened:
                    shortened_url = surl
                    break

            nurl = NUrl(short_url=shortened_url, original_url=url)
            # INSERT INTO nurls() here essentially
            self.__shortened[shortened_url] = nurl
            self.__originals[url] = nurl
        return self.__originals[url]

    def get_by_shortened(self, nurl):
        # SELECT original_url FROM nurls where shortened_url = {nurl}
        # Also, in a high capacity system, we could put use a combination of redis
        # and even an in memory store for caching, to avoid SQL hits
        if nurl in self.__shortened:
            return self.__shortened[nurl]
        return None

