import urllib.parse
from typing import Optional, Dict


def is_valid(url: str) -> bool:
    """
    >>> is_valid('https://www.baidu.com/')
    True

    :param url:
    :return:
    """
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def quote(url: str) -> str:
    """
    >>> quote('abc def')
    'abc%20def'

    :param url:
    :return:
    """
    return urllib.parse.quote(url)


def unquote(url: str) -> str:
    """
    >>> unquote('abc%20def')
    'abc def'

    :param url:
    :return:
    """
    return urllib.parse.unquote(url)


def encode(params: Dict) -> str:  # noqa
    """
    >>> encode({'a': 1, 'b': 2, 'c': 3})
    'a=1&b=2&c=3'

    :param params:
    :return:
    """
    return urllib.parse.urlencode(params)


def decode(url: str) -> Dict:  # noqa
    """
    >>> decode('a=1&b=2&c=3')
    {'a': '1', 'b': '2', 'c': '3'}

    :param url:
    :return:
    """
    params = dict()

    kvs = url.split('?')[-1].split('&')
    for kv in kvs:
        k, v = kv.split('=', 1)
        params[k] = unquote(v)

    return params


def join_params(url: str, params: Optional[Dict]) -> str:
    """
    >>> join_params('https://www.baidu.com/s', {'ie': 'UTF-8', 'wd': 'abc'})
    'https://www.baidu.com/s?ie=UTF-8&wd=abc'

    :param url: 
    :param params: 
    :return: 
    """
    if not params:
        return url

    params = encode(params)
    separator = '?' if '?' not in url else '&'
    return url + separator + params
