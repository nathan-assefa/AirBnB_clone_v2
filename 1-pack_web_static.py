#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
""" To generate archive file form webstatic folder """


def do_pack():
    """ Generating archive file """
    
    local('mkdir -p versions')
    
    file_path = "versions/web_static_{}.tgz"\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    
    archive_file = local("tar -cvzf {} web_static".format(file_path))
    
    if archive_file.failed:
        return None
    return archive_file
