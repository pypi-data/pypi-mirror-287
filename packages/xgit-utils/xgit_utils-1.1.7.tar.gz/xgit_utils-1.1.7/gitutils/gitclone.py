#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
"""
git clone tools
"""
import argparse
import os
import sys
from urllib import parse

import gitutils
from gitutils import utils

DESCRIPTION = 'git clone'


def _exec_clone(target_dir: str, url: str, prefix: str):
    """
    clone cmd
    :param target_dir:
    :param url:
    :param prefix:
    :return:
    """
    parse_result = parse.urlparse(url=url)
    parse_path = parse_result.path.strip()
    hostname = parse_result.hostname.strip()
    if parse_path.endswith("git"):
        parse_path = parse_path[0:len(parse_path) - 4]
    paths = [x for x in parse_path.split("/") if x != ""]
    size = len(paths)
    if size >= 2:
        group = paths[0:size - 1]
        name = paths[size - 1]
        # github.com + .git
        if (hostname == "github.com") and (not url.endswith(".git")):
            if url.endswith("/"):
                url = url[0:len(url) - 1].strip() + ".git"
            else:
                url = url.strip() + ".git"
        utils.my_print('>> %s begin to clone %s from %s' % (
            utils.Color.green(prefix), utils.Color.red(name), url))
        cmd_clone = "git clone --mirror %s" % (url,)
        group_path = os.path.join(target_dir, os.path.sep.join(group))
        if not os.path.exists(group_path):
            os.makedirs(group_path)
        if not os.path.exists(os.path.join(group_path, name + ".git")):
            os.chdir(group_path)
            os.system(cmd_clone)
        else:
            utils.my_print_red(">> Repo exists")
    else:
        utils.my_print_red(">> The 'git URL' format is incorrect")


def cmd_clone(args):
    """git clone
    :return:
    """
    target_dir: str = args.target_dir
    file: str = args.url_file
    gitutils.set_proxy(args=args)
    if file.strip() and os.path.exists(file) and os.path.isfile(file):
        with open(file, 'r') as f:
            lines = f.readlines()
            size = len(lines)
            if size > 0:
                for index, url in enumerate(lines):
                    _exec_clone(target_dir, url.strip(), prefix="[{0}/{1}]".format(index + 1, size))
            else:
                utils.my_print_red("The target file does not contain 'git URL'")
    elif file.startswith("http") or file.startswith("git"):
        _exec_clone(target_dir, file, prefix="[{0}/{1}]".format(1, 1))
    else:
        utils.my_print_red(">> The format of the target file is incorrect")


def set_args(parser):
    """
    set args
    :param parser:
    :return:
    """
    parser.add_argument('--target_dir', type=str,
                        help=u'Clone the Repo to the directory【default:{0}】'.format(gitutils.DEFAULT_GITHUB),
                        default=gitutils.DEFAULT_GITHUB)
    parser.add_argument("url_file", type=str, help=u'git URL or File')
    gitutils.parser_proxy(parser=parser)
    parser.set_defaults(func=cmd_clone)


def execute():
    """execute point
    :return:
    """
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog='make it easy')
    set_args(parser)
    # parser args
    args = parser.parse_args()
    args.func(args)


def test():
    """
    test
    :return:
    """
    sys.argv.append("--target_dir")
    sys.argv.append("/Users/seven/Desktop/abc")
    sys.argv.append("https://github.com/PhilJay/MPAndroidChart/")


if __name__ == '__main__':
    sys.argv.append("/Users/seven/Desktop/git.txt")
    execute()
