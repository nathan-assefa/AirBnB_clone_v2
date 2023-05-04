#!/usr/bin/python3
"""
    Compiling .tar file to uncompress the file before we send
    it to the remote server
"""


from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """ This function packes different files into .tar file """

    # First create a directory 'versions' if it is not exist
    if not os.path.isdir('./versions'):
        os.makedirs('./versions')
        # here we can also use the 'local' method
        # local(mkdir -p versions)

    # Creating a file to pack the archive
    arch_name = '/versions/web_static_{}.tgz'.format(
            datetime.now().strftime("%Y%m%d%H%M%S")
            )

    # Creating .tar file using tar command line tool
    archive_file = local('tar -cvzf arch_name web_static')

    try:
        return archive_file
    except Exception:
        return None
