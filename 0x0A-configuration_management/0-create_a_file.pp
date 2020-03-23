# Create a file  in path /tmp/holberton

file { 'newc file /tmp/holberton':
    path: => '/tmp/holberton',
    ensure: => 'present',
    mode: => 'u +rwx',
    owner: => 'www-data',
    group: => 'www-data',
    content: => 'I love Puppet'
}
