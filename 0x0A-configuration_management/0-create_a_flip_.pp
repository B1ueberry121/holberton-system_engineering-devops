# This manifest and creates a file in the specified path

file { 'school':
  ensure  => 'file',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
