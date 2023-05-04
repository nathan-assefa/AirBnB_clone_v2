#!/usr/bin/python3
""" This script compiles archives to send to server """


from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """ packing web_static directory """
    if not os.path.exists('./versions'):
        os.makedirs('./versions')

    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.failed:
        return None
    else:
        return filename
