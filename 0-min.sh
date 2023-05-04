#!/usr/bin/env bash
#setting up your web servers for the deployment of web_static


# install nginx if not exist
if [! -x /usr/sbin/nginx]
then
	sudo apt-get -y update
	sudo apt-get -y install
fi

# creating a folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# the 'tee' command would write to the file index.html if the file exists,
# + otherwise it creates the file and wirtes into it.
echo "Hello from vagrant world" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link. The -f option forces the symbolic link creation
# and if the symbolic link /data/web_static/current already exists,
# it will be replaced by the new symbolic link.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# -R flag give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Creating alias
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restarig nginx
sudo service nginx restart

