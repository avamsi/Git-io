import sys
PY3 = sys.version > '3'

url = 'http://git.io/'

def git_io(req_url):
    if PY3:
        import urllib.request
        urlopen = urllib.request.urlopen
        data = bytes(
            urllib.parse.urlencode(
                {'url': req_url}
            ), encoding='ascii'
        )
        Error = urllib.error.HTTPError
    else:
        import urllib
        urlopen = urllib.urlopen
        data = urllib.urlencode({'url': req_url})
        Error = KeyError
    try:
        return urlopen(url, data).headers['location']
    except Error:
        return 'Must be a GitHub.com URL.'

# demo
req = 'https://github.com/krikx'
print(git_io(req))
