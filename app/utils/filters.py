# -*- coding:utf-8 -*-
from app.utils.aes import AESUtil


def math_mod(i, mod=5):
    i = int(i)
    return i % mod


def str_split(s, sep=','):
    """
    split strings
    :param s:
    :param sep:
    :return:
    """
    s = s if s else ''
    return str(s).split(sep)


def get_tuple(t, index):
    if not isinstance(t, tuple):
        t = tuple(t)
    return t[index] if t and len(t) > 0 else ()


def get_list(l, index):
    """
    get list an specified element
    :param l:
    :param index:
    :return:
    """
    return l[index] if l and len(l) > 0 else []


def get_sub_list(l, start, end):
    """
    get sub list
    :param l:
    :param start:
    :param end:
    :return:
    """
    return l[start:end] if l and len(l) > 0 else []


def b64encode(s):
    """
    AES encrypt
    :param s:
    :return:
    """
    return AESUtil.encrypt(s)


def b64_str_decode(b):
    """
    AES decrypt
    :param b:
    :return:
    """
    return AESUtil.decrypt(b)

