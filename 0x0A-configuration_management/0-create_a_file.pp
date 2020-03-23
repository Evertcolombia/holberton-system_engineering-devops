# Create a file  in path /tmp/holberton

file { 'newc file /tmp/holberton':
    ensure  => 'present',
    path    => '/tmp/holberton',
    mode    => 'u+rwx',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
