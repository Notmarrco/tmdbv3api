from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class List(TMDb):
    _urls = {
        'details': '/list/%s'
    }


    def details(self, list_id):
        """
        Get list details by id.
        :param list_id:
        :return:
        """
        return self._get_obj(self._call(self._urls['details'] % str(list_id), ''), key='items')
