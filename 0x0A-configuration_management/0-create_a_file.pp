# This manifest and creates a file in the specified path

file { '/tmp/school' :
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
}
