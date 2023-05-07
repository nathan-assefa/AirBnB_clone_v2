# puppet manifest preparing a server for static content deployment

puppet apply -e '
package { "nginx":
  ensure => installed,
}

file { ["/data", "/data/web_static", "/data/web_static/releases", "/data/web_static/shared", "/data/web_static/releases/test"]:
  ensure  => directory,
  owner   => "ubuntu",
  group   => "ubuntu",
  recurse => true,
}

file { "/data/web_static/releases/test/index.html":
  ensure  => file,
  owner   => "ubuntu",
  group   => "ubuntu",
  content => "<html><body>Test Page</body></html>",
}

file { "/data/web_static/current":
  ensure => link,
  target => "/data/web_static/releases/test",
  owner  => "ubuntu",
  group  => "ubuntu",
  force  => true,
}

file { "/etc/nginx/sites-available/default":
  ensure  => file,
  content => "
    server {
        listen 80;
        listen [::]:80;

        root /data/web_static/current;

        index index.html;

        location /hbnb_static {
            alias /data/web_static/current;
            index index.html;
        }
    }
  ",
  notify => Service["nginx"],
}

service { "nginx":
  ensure    => running,
  enable    => true,
  subscribe => File["/etc/nginx/sites-available/default"],
}'
