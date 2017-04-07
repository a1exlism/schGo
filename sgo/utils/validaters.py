# -*- coding: utf-8 -*-
"""
All Validate and Filter Functions
"""

import re


def clean_str(src):
    """
    
    :param src: str to clean
    :return: True or False, Processed String
    """
    src = str(src)
    if len(src) == 0 or '$' in src:
        return False, None
    return True, src


_USER_ID_REGEX = re.compile(r'\w{6,16}', re.U)


def check_id(user_id):
    """
    user_id 
    :param user_id: 
    :return: 
    """
    result = _USER_ID_REGEX.match(user_id)

    return True if result.string == user_id else False


_URL_REGEX = re.compile(
    r'^(?:[a-z0-9\.\-]*)://'  # scheme is validated separately
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
_URL_SCHEMES = ['http', 'https', 'ftp', 'ftps']


def check_url(url):
    scheme = url.split('://')[0].lower()
    if scheme not in _URL_SCHEMES:
        return False

    if not _URL_REGEX.match(url):
        return False

    return True


def check_email(email):
    pass