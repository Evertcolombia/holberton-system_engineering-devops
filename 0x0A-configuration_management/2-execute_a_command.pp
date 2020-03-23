# manifiest that kill a process

exec { 'kill a process':
    path    => '/usr/bin',
    command => '/usr/bin/pkill killmenow'
}
