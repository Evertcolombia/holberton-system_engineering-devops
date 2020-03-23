# install puppet-lint (2.1.1)  using puppet resource

package { 'puppet-lint':
    ensure   => '2.1.1',
    name     => 'puppet-lint', 
    provider => 'gem'
}
