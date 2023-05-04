#!/usr/bin/python3
"""
    Distributing an archive to your web servers,
    using the function do_deploy:
"""

from fabric.api import run, local, put, env
import os

env.hosts = ["54.173.114.81", "54.210.188.25"]


def do_deploy(archive_path):
    """Deploying static files to web servers"""
    # check if the path exits
    if not os.path.exists(archive_path):
        return False

    try:
        # Setting up required parameters(follow steps of 1, 2, & 3)
        # 1. Extracting the archive file from the path
        arch_file = archive_path.split("/")[-1]

        # 2. Removing the extension .tar from the file
        no_ext = "/data/web_static/releases/" + arch_file.replace(
                ".tar.gz", ""
                )

        # 3. Adjusting the location where the archive is stored temporarily
        remote_temp = "/tmp/{}".format(arch_file)

        # Storing the archive to the remote server using 'put' command
        put(archive_path, "/tmp/")

        # Here the archive is in the remote server of '/tmp/' folder.
        # We can uncompress the archive from the /tmp/ location
        run("mkdir -p {}".format(no_ext))
        run("tar -xzf {} -C {}".format(remote_temp, no_ext))

        # We can now remove the archive from /tmp/ directory
        run("rm {}".format(remote_temp))

        # Now, we have uncompressed file in the directory 'no_ext'
        # Let us mv the the contents of the uncompressed file
        run("mv {}/web_static/* {}".format(no_ext, no_ext))

        # We can now remove the old one
        run("rm -rf {}/web_static".format(no_ext))

        # Let us remove the old symbolic link
        run("rm /data/web_static/current")

        # Let us create the new symbolic link
        run("ln -s {} /data/web_static/current".format(no_ext))

        return True
    except Exception:
        return False