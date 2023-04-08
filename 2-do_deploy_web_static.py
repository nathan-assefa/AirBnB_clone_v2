#!/usr/bin/python3
"""
The goal for this project is deploying the contents of the web_static
directory in a server. There are steps that need to be followed in order
to deploy the application. First, We need to compress all the files and
folders within the web_static directory using tar command line tool.
Second, we need to create a folder in the server in order to uncompress the
the archives. Third, we need to to uncompress the archive and put the original
file in the in aa folder that we will create. Since we want our path to be
unique, we use iso format string ofdatetime module.
Finally we need to remove all the
archive from the server along with the the symbolic link.
"""
from fabric.api import local, run, env
from datetime import datetime
import os


env.hosts = ['35.153.52.120', '52.91.183.3']


def do_deploy(archive_path):
    """ Deploying an webstatic app"""

    try:
        # First deploy all the archive into the /tmp directory in the server
        # Here we need to use 'put' command that uses the hosts to
        # deploy the archive in a server
        put('archive_path', '/tmp/')

        # Create a folder to uncompress the archive.
        # The folder name is going to be
        # /data/web_static/releases/<archive filename without extension>
        # since we do not have '<archive filename without extension>',
        # we ceate it it
        # Creating a file '<archive filename without extension>'

        file_with_ext = archive_path.split('/')[-1]
        file_without_ext = file_with_ext.split('.')[0]

        # Know we have the file name so that we can
        # uncompress the archive and put the
        # uncompressed folder in this file.
        # Here we use the 'tar' command line tool in order to unzip the archive
        # '-x' flag is used for uncompress the archive
        # 'z' to use gzip
        # 'f' to indicate the file whereby the archive exists
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file_with_ext, file_without_ext))

        # Moving the files from web_static directory
        run('mv /data/web_static/releases/{}/web_static /data/web_static\
                /releases/{}'.format(file_without_ext, file_without_ext))

        # Removing the web_static directory
        run('rm -rf /data/web_static/releases/{}\
                /web_static'.format(file_without_ext))

        # Now we have uncompressed folder. Therefor,
        # we can rermove the archive
        run('rm /tmp{}'.format(file_with_ext))

        # Removing the symbolic link
        run('rm -rf /data/web_static/current')

        run('ln -sf /data/web_static/releases/{} /data/\
                web_static/current'.format(file_without_ext))
        return True
    except Exception:
        return False
