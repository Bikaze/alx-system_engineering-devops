# This script uses Puppet to create a manifest that kills a process named killmenow.

exec { 'killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => 'shell',
    returns  => [0, 1]
}
