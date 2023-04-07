#!/usr/bin/env bash
# Writing a Fabric script (based on the file 1-pack_web_static.py)
# +that distributes an archive to your web servers,
# +using the function do_deploy:

if [ ! -x /usr/sbin/nginx ]
then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi

# Creating folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creating an html file with fack content within it
echo "Hey this is Nathan" > sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving owner ship for ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Editing nginx configuarion file
sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Restarig nginx
sudo service nginx restart
