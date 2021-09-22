# This would actually be a SqlAlchemy Model
class NUrl(object):
    # i.e.
    # __tablename__ = 'users'
    # id = Column('id', Integer, primary_key=True)

    def __init__(self, short_url=None, original_url=None):
        self.__short_url = short_url
        self.__original_url = original_url

    @property
    def short_url(self):
        return self.__short_url

    @property
    def original_url(self):
        return self.__original_url
