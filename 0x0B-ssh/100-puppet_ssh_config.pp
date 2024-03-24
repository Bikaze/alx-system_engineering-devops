# puppet script to create a ~/.ssh/config file

file { '/home/bkz/.ssh/config':
    ensure  => file,
    content => 'Host 54.172.242.22
                IdentityFile ~/.ssh/school
                PasswordAuthentication no'
}
