# puppet manifest preparing a server for static content deployment

exec {'/usr/bin/env apt-get -y update':}
-> exec {'/usr/bin/env apt-get -y install nginx':}

-> exec {'/usr/bin/env mkdir -p /data/web_static/releases/test/':}
-> exec {'/usr/bin/env mkdir -p /data/web_static/shared/':}

-> exec {'Write Hello World in index with tee command':
  command => '/usr/bin/env echo "Hello Puppet" | sudo tee /data/web_static/releases/test/index.html',
}

-> file {'/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
}

-> exec {'Add new configuration to NGINX':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

-> exec {'/usr/bin/env chown -R ubuntu:ubuntu /data':}

-> exec {'/usr/bin/env service nginx restart':}
