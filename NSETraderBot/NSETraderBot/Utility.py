from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import six
import json


class TraderUtility:


    def nse_headers(self):
        return {'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Host': 'www1.nseindia.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                'X-Requested-With': 'XMLHttpRequest'
                }


    def nse_opener(self):
        cj = CookieJar()
        return build_opener(HTTPCookieProcessor(cj))


    def byte_adaptor(self, fbuffer):
        strings = fbuffer.read().decode('latin-1')
        fbuffer = six.StringIO(strings)
        return fbuffer


    def render_response(self, data, as_json=False):
        if as_json is True:
            return json.dumps(data)
        else:
            return data
