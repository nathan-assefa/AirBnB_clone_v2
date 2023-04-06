#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
""" To generate archive file form webstatic folder """


def do_pack():
<<<<<<< HEAD
    """ Generating archive file """
    
    local('mkdir -p versions')
    
    file_path = "versions/web_static_{}.tgz"\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    
    archive_file = local("tar -cvzf {} web_static".format(file_path))
    
    if archive_file.failed:
=======
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = 'versions/web_static_{}.tgz'\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    #if os.path.isdir("versions") is False:
        #if local("mkdir -p versions").failed is True:
            #return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
>>>>>>> e0780c697da14b31da308066152bc5d7bc9560d4
        return None
    return archive_file
