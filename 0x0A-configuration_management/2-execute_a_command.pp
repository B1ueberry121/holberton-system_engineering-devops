# Kills kill me now
exec { 'pkill':
command => 'pkill -9 killmenow',
path    => '/usr/bin/'
}
