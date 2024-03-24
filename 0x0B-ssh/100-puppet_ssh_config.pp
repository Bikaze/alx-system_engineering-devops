# puppet script to make a change to our ssh config file

file_line { 'private key':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'no PasswordAuth':
    ensure => 'present',
    line   => 'PasswordAuthentication no',
    path   => '/etc/ssh/ssh_config',
}
