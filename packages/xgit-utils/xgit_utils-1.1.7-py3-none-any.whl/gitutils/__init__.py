# -*- coding: utf-8 -*-
"""
git utils
"""
import os

import gitutils.utils
import gitutils.version

DEFAULT_PROXY = "127.0.0.1:1087"
DEFAULT_GITHUB = os.path.expanduser("~/Mirror/github")

DEFAULT_THREAD_SIZE = 6


def parser_proxy(parser):
    """
    set proxy
    :param parser:
    :return:
    """
    # use proxy
    parser.add_argument('-u', '--use_proxy', help='use proxy', action='store_true', default=False)
    # proxy
    parser.add_argument('-p', '--proxy', help='http[s] proxy【default:{0}】'.format(DEFAULT_PROXY), type=str,
                        default=DEFAULT_PROXY)


def set_proxy(args):
    """
    set proxy
    :param args:
    :return:
    """
    try:
        use_proxy = args.use_proxy
        proxy = args.proxy
        if use_proxy and proxy:
            if utils.is_connected(url=proxy):
                os.environ.setdefault(key="http_proxy", value="http://{}".format(proxy))
                os.environ.setdefault(key="https_proxy", value="http://{}".format(proxy))
    except AttributeError:
        pass
