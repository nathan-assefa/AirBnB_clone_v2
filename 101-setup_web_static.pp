# puppet manifest preparing a server for static content deployment

exec {'/usr/bin/env apt-get -y update':}
-> exec {'/usr/bin/env apt-get -y install nginx':}

-> exec {'/usr/bin/env mkdir -p /data/web_static/releases/test/':}
-> exec {'/usr/bin/env mkdir -p /data/web_static/shared/':}

-> file {'/data/web_static/releases/test/index.html':
ensure => present,
content => 'echo "Hi everyone | This is Nathan" | sudo tee /data/web_static/releases/test/index.html',
}

-> file {'/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
}

-> exec {'Inserting line':
    command => '/usr/bin/env sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
}

-> exec {'/usr/bin/env chown -R ubuntu:ubuntu /data':}

-> exec {'/usr/bin/env service nginx restart':}
