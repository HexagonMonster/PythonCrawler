from py_version import py_version
import socket
if py_version == 3:
    from urllib import request as urllib
else:
    import urllib2 as urllib


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        try:
            response = urllib.urlopen(url, timeout=10)

            if response.getcode() != 200:
                return None

            return response.read()
        except Exception as e:
            raise e