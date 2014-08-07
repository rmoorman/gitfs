from abc import ABCMeta


class View(object):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        self.args = args

        for attr in kwargs:
            setattr(self, attr, kwargs[attr])

    def getattr(self, *args, **kwargs):
        return {
            'st_uid': self.uid,
            'st_gid': self.gid,
        }
