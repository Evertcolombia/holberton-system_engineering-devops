# update headers response to nginx

exec { 'apt-get':
    path    => '/usr/bin',
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['apt-get']
}

service { 'nginx':
    ensure  => running
}

exec { 'mkdir-directory':
    path    => '/bin',
    command => '/bin/mkdir -p /var/www/html',
    require => Package['nginx']
}

file { '/var/www/html/index.html':
    ensure  => file,
    path    => '/var/www/html/index.html',
    content => 'Holberton School',
    require => Exec['mkdir-directory'],
}

exec { 'header_response':
    command => '/bin/sed -i "60i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
    require => Package['nginx']
}

exec { 'restart':
    command => '/bin/service nginx restart',
    require => Exec['header_response']
}
