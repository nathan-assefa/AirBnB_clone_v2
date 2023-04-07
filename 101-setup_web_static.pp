# Implementing task 0 using puppet

exec {'/usr/bin/apt-get -y update':
    -> package => {'nginx':
        provider => apt,
        ensure => installed,
    }
    
    -> file {'/data/web_static/releases/test/':
        ensure => directory,
    }
    -> file {'/data/web_static/shared/':
        ensure => directory,
    }
    -> file {'/data/web_static/releases/test/index.html':
        ensure => present,
        content => 'Hi everyone |This is Nathan',
    }
    -> file {'Symbolic link':
        path => '/data/web_static/current',
	ensure => link,
        target => '/data/web_static/releases/test/',
    }
}

exec {'Inserting line':
    command => 'sudo sed -i "/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
}

exec {'sudo /usr/bin/env service nginx restart'}
