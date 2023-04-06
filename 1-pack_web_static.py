#!/usr/bin/python3
""" This script genertes archive files from webstatic folder """
from fabric.api import local
from datatime import datetime


def do_pack():
    """ Generating archive file """
    local("mkdir -p versions")
    file = 'versions/web_static_{}.tgz'\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))

    archive_file = local("'tar -cvzf {} web_static'.format(file)")
    if archive_file.failed:
        return None
    return file
