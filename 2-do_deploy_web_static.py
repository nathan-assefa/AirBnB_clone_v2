#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
using the function do_deploy
"""
from fabric.api import env, run, put, hosts
# from datetime import datetime
import os

env.hosts = ['35.153.52.120', '52.91.183.3']


def do_deploy(archive_path):
    """ function distrubtes an archive to my web servers
    """
    path_existence = os.path.exists(archive_path)
    if path_existence is False:
        return False
    try:
        file_with_ext = archive_path.split('/')[-1]
        file_without_ext = archive_path.split('.')[0]
        folder = '/data/web_static/releases/{}'.format(file_without_ext)
        put(archive_path, '/tmp')
        run('mkdir -p /data/web_static/releases/{}'.format(file_without_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file_with_ext, file_without_ext))
        # Moving the files from web_static directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static\
                /releases/{}/'.format(file_without_ext, file_without_ext))

        # Removing the web_static directory
        run('rm -rf /data/web_static/releases/{}\
                /web_static'.format(file_without_ext))

        # Now we have uncompressed folder. Therefor,
        # we can rermove the archive
        run('rm /tmp/{}'.format(file_with_ext))

        # Removing the symbolic link
        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/\
                web_static/current'.format(file_without_ext))
        return True
       #run('rm /tmp/{}'.format(file_with_ext))
       # run('mv {}/web_static/* {}'.format(folder, folder))
       # run('rm -rf {}/web_static'.format(folder))
       # current = '/data/web_static/current'
       # run('rm -rf {}'.format(current))
       # run('ln -s {}/ {}'.format(folder, current))
       # return True
    except Exception:
        return False
