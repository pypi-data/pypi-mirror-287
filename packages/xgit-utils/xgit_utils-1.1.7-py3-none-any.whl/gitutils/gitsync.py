#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
"""
git sync tools
"""

import argparse
import os
import re
import sys
import time
from multiprocessing import Pool
from urllib import parse

import gitutils
from gitutils import utils
from gitutils import version

__version__ = '1.0.0'
DESCRIPTION = 'git sync {0}'


def scan_repo(input_dir, git_dir_list):
    """ scan repo
    :param input_dir:
    :param git_dir_list:
    :return:
    """
    sub_dir_list = [x for x in os.listdir(
        input_dir) if os.path.isdir(os.path.join(input_dir, x))]
    if "branches" in sub_dir_list and "objects" in sub_dir_list:
        git_dir_list.append(input_dir)
    elif ".git" in sub_dir_list:
        pass
    elif ".svn" in sub_dir_list:
        pass
    else:
        for sub_dir in sub_dir_list:
            scan_repo(os.path.join(input_dir, sub_dir), git_dir_list)


def get_repo(input_dir, filter_host=['']):
    """ get repo
    :param input_dir:
    :param filter_host:
    :return:
    """
    temp_list = []
    remote_list = []
    git_list = []
    url_list = []
    scan_repo(input_dir=input_dir,
              git_dir_list=temp_list)
    for git_dir in temp_list:
        os.chdir(git_dir)
        cmd_result = os.popen('git remote -v').read()
        origin_list = re.findall(r'origin	(.*?) \(push\)', cmd_result)
        if origin_list:
            origin = origin_list[0].strip()
            # -------
            if origin.startswith('git'):
                temp_host = re.findall(r'@(.*?):', origin)
                if temp_host:
                    host = temp_host[0].strip()
            elif origin.startswith('http'):
                parse_result = parse.urlparse(url=origin)
                """:type: urllib.parse.ParseResult"""
                host = parse_result.hostname
            else:
                pass
            if host not in remote_list:
                remote_list.append(host)
            # -------
            is_ok = True
            if filter_host and len(filter_host) > 0:
                for host in filter_host:
                    if host in origin:
                        is_ok = False
                        break
            if is_ok:
                git_list.append(git_dir)
                url_list.append(origin)
    return remote_list, git_list, url_list


def exec_fetch(git_dir):
    """git fetch
    :param git_dir:
    :return:
    """
    os.chdir(git_dir)
    os.system('git fetch origin')


def repos_fetch(target_dir, git_list, thread_size):
    """
    repos fetch
    :param target_dir:
    :param git_list:
    :param thread_size:
    :return:
    """
    if thread_size <= 0:
        thread_size = 1
    pool = Pool(processes=thread_size)
    size = len(git_list)
    for index, git_dir in enumerate(git_list):
        pool.apply_async(repo_fetch, args=(git_dir, target_dir, size, index))
    pool.close()
    pool.join()


def repo_fetch(repo, target_dir, size, index):
    """
    repo fetch
    :param repo:
    :param target_dir:
    :param size:
    :param index:
    :return:
    """
    utils.my_print('[{0}/{1}] - {2}'.format(index + 1,
                                            size, repo.replace(target_dir, '')))
    exec_fetch(git_dir=repo)


def cmd_sync(args):
    """git sync
    :param args:
    :return:
    """
    # target dir
    target_dir = args.target_dir
    # thread size
    thread_size = args.thread
    # filter host
    filter_host = args.filter_host
    # list remote
    list_remote = args.list_remote
    # list repo
    list_repo = args.list_repo
    # sync repo
    repo = args.repo
    # show notify
    notify = args.notify
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # proxy
    gitutils.set_proxy(args=args)
    """:type:str"""
    start_time = time.time()
    utils.my_print('>> Start: {0}'.format(time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(start_time))))
    remote_list, git_list, url_list = get_repo(input_dir=target_dir,
                                               filter_host=filter_host)
    if list_remote:
        if remote_list:
            size = len(remote_list)
            for index, remote in enumerate(remote_list):
                utils.my_print('[{0}/{1}] - {2}'.format(index + 1, size, remote))
            utils.my_print_green('-----------------------')
            url_size = len(url_list)
            for index, url in enumerate(url_list):
                utils.my_print('[{0}/{1}] - {2}'.format(index + 1, url_size, url))
        else:
            utils.my_print_red('>> no remote')
    elif list_repo:
        if url_list:
            for url in url_list:
                print(url)
    elif repo:
        repos = []
        repo_list = [x for x in repo.split(",") if x != ""]
        for x in git_list:
            for y in repo_list:
                if x.lower().find(y.lower()) > -1:
                    repos.append(x)
                    break
        repos_fetch(target_dir=target_dir, git_list=repos, thread_size=thread_size)
    else:
        repos_fetch(target_dir=target_dir, git_list=git_list, thread_size=thread_size)
    end_time = time.time()
    utils.my_print('>> End {0}'.format(time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(end_time))))
    run_time = int(end_time - start_time)
    utils.my_print('>> Time: {0}'.format(utils.time_count(run_time)))
    if notify:
        utils.notify(content="Done", title="GitSync")


# --------------------------------------------------------------------

def set_args(parser):
    """
    set args
    :param parser:
    :return:
    """
    parser.add_argument('-d', '--target_dir', type=str, default=gitutils.DEFAULT_GITHUB,
                        help='target dir【default:{0}】'.format(gitutils.DEFAULT_GITHUB))
    parser.add_argument('-t', '--thread', type=int, default=gitutils.DEFAULT_THREAD_SIZE,
                        help="number of threads 【default:{0}】".format(gitutils.DEFAULT_THREAD_SIZE))
    parser.add_argument('-f', '--filter_host',
                        action='append', help='filter host')
    # sync repo
    parser.add_argument('-r', '--repo', type=str,
                        help="sync repo - [okhttp,ffmpeg,...]")
    # show remote list
    parser.add_argument('--list_remote',
                        help='show remote list', action='store_true', default=False)
    # show repo list
    parser.add_argument('--list_repo', action='store_true', default=False, help='show repo list')
    # show notify
    parser.add_argument('--notify', action='store_true', default=False, help='show notify')
    gitutils.parser_proxy(parser=parser)
    parser.set_defaults(func=cmd_sync)


def execute():
    """execute point
    :return:
    """
    parser = argparse.ArgumentParser(
        description=DESCRIPTION.format(version.VERSION), epilog='make it easy')
    set_args(parser)
    # parser args
    args = parser.parse_args()
    args.func(args)


def test():
    sys.argv.append('-d')
    sys.argv.append('/Users/seven/mirror')

    # sys.argv.append('-f')
    # sys.argv.append('gitee.com')
    #
    # sys.argv.append('-f')
    # sys.argv.append('github.com')

    # sys.argv.append('-f')
    # sys.argv.append('android.googlesource.com')

    # sys.argv.append('-f')
    # sys.argv.append('gerrit.googlesource.com')

    # sys.argv.append('-f')
    # sys.argv.append('webrtc.googlesource.com')

    # sys.argv.append('-r')
    # sys.argv.append('okhttp,ffmpeg')


if __name__ == '__main__':
    test()
    execute()
