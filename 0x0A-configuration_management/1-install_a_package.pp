# Ensures the gem linter is installed
package { 'puppet-line' :
ensure   => installed,
provider => 'gem',
}
