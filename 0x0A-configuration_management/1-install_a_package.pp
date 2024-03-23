# This script uses Puppet to install flask from pip3.

package { 'python3-pip':
  ensure => 'present',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0" && /usr/bin/pip3 show werkzeug | grep -q "Version: 2.1.1"',
  require => Package['python3-pip'],
}
