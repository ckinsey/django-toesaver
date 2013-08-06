from django.core.cache import cache
from django.conf import settings


class ViewCounter(object):

    def __init__(self, path=None):
        """
        Ensures that a URL path is referenced for this counter.
        """
        if not path:
            raise TypeError("Must pass in a path for view counter object")
        self.path = path

    def get_cache_key(self):
        return "toesaver-%s" % self.path

    def get_viewers(self):
        """
        Returns a list of usernames browsing the current view
        """
        key = self.get_cache_key()
        viewers = cache.get(key)
        if viewers is not None:
            return viewers
        return []

    def set_viewer(self, user):
        """
        Examines the current list of users in cache.  If the current user is not listed,
        he is added to the list and it is recached.
        """
        key = self.get_cache_key()
        viewers = self.get_viewers()
        if not user.username in viewers:
            viewers.append(user.username)
            cache.set(key, viewers, settings.TOESAVER_VIEW_TIMEOUT)

