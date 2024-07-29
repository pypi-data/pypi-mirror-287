# -*- coding: utf-8 -*-
import getpass
import os
import platform
import socket
import time
from time import gmtime
from time import strftime


def is_connected(url: str) -> bool:
    try:
        hostname = url.split(':')[0]
        port = int(url.split(':')[1])
        socket.create_connection((hostname, port))
        return True
    except OSError:
        pass
    return False


def notify(content: str, title: str = None):
    """
    show notify
    """
    try:
        if not title:
            title = getpass.getuser()
        if is_mac():
            mac_notify(content=content, title=title)
        else:
            pass
    except Exception as e:
        print(str(e))


def mac_notify(content: str, title: str):
    """
    mac notify
    """
    os.system(
        'osascript -e \'display notification "{0}" with title "{1}"\''.format(content, title))


def time_count(count) -> str:
    """
    time count
    :param count:
    :return:
    """
    return strftime("%H:%M:%S", gmtime(count))


def is_root() -> bool:
    """
    is root
    :return:
    """
    return os.geteuid() == 0


def is_mac() -> bool:
    """
    is Mac
    :return:
    """
    return platform.system() == "Darwin"


def my_print(message: str):
    """
    print
    :param message:
    :return:
    """
    print(Color.green(time.strftime('%Y-%m-%d %H:%M:%S -')), message)


def my_print_red(message: str):
    """
    print red
    :return:
    """
    print(Color.red(time.strftime('%Y-%m-%d %H:%M:%S -')), Color.red(message))


def my_print_green(message: str):
    """
    print green
    :return:
    """
    print(Color.green(time.strftime('%Y-%m-%d %H:%M:%S -')), Color.green(message))


class Color(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BlUE = '\033[94m'
    END = '\033[0m'

    @classmethod
    def red(cls, string):
        return cls.RED + string + cls.END

    @classmethod
    def green(cls, string):
        return cls.GREEN + string + cls.END

    @classmethod
    def yellow(cls, string):
        return cls.YELLOW + string + cls.END

    @classmethod
    def blue(cls, string):
        return cls.BlUE + string + cls.END


if __name__ == '__main__':
    print(is_connected(url="127.0.0.1:1087"))
