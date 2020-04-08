from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import six, json, re


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


    def clean_server_response(self, resp_dict):
        d = {}
        for key, value in resp_dict.items():
            d[str(key)] = value
        resp_dict = d
        for key, value in resp_dict.items():
            if type(value) is str or isinstance(value, six.string_types):
                if re.match('-', value):
                    try:
                        if float(value) or int(value):
                            dataType = True
                    except ValueError:
                        resp_dict[key] = None
                elif re.search(r'^[0-9,.]+$', value):
                    resp_dict[key] = float(re.sub(',', '', value))
                else:
                    resp_dict[key] = str(value)
        return resp_dict