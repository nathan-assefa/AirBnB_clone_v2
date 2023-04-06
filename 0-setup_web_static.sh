#!/usr/bin/env bash
# Writing a Bash script that sets up your web servers for the deployment of web_static

#installing nginx

sudo apt-get -y update
sudo apt-get -y install nginx

# Creating differnt folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Writing into a file
# echo "<h3>Hi everyone, this is Nathan</h3>" > sudo tee /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.htm

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name .*;/a location /hbnb_static {\nalias /data/web_static/current;\n}\n" /etc/nginx/sites-available/default
sudo service nginx restart
