# Implementing task 0 using puppet

exec {'/usr/bin/env apt-get -y update'}
-> package {'nginx':
    provider => apt,
    ensure => installed,
}

-> exec {'sudo /usr/bin/env mkdir -p /data/web_static/releases/test/'}
-> exec {'sudo /usr/bin/env mkdir -p /data/web_static/shared/'}

-> file {'/data/web_static/releases/test/index.html':
ensure => present,
content => 'Hi everyone |This is Nathan',
}

-> file {'Symbolic link':
    path => '/data/web_static/current',
    ensure => link,
    target => '/data/web_static/releases/test/',
}

-> exec {'Inserting line':
    command => 'sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
}

-> exec {'sudo /usr/bin/env chown -R ubuntu:ubuntu /data'}

-> exec {'sudo /usr/bin/env service nginx restart'}
