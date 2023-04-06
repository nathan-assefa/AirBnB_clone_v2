#!/usr/bin/env bash
# setup web static server

sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

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
