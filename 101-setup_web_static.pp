# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Directories to create
$directories = [
  '/data',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test',
]

# Create directories
file { $directories:
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<html><body>Test Page</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  force  => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80;
        listen [::]:80;

        root /data/web_static/current;

        index index.html;

        location /hbnb_static/ {
            alias /data/web_static/current;
            index index.html;
        }
    }
  ",
  notify => Service['nginx'],
}

# Set ownership of /data/ directory
exec { 'set_ownership_data_directory':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data/',
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
