## for-cli

Simple CLI to interact with the REST API for foreman or the smart-proxy. http://theforeman.org/
Written in Python.

Make sure to change the default username/password and baseurl for your foreman installation
or use the --username/password/url/port flags.

### Query for facts

#### Get all hosts and values for a specific fact (kernelversion)

    for-cli -q facts kernelversion

#### Get all facts and values for a specific host (FQDN)

    for-cli -q facts --host=host.example.com

### Query for status

#### System status (result ok/failed, database lag in miliseconds)

    for-cli -q status

#### Summary statistcs (total hosts, active hosts, hosts in error etc)

    for-cli -q dashboard

### Query for reports

#### Retrieve the lastest report

    for-cli -q reports

#### Retrieve the latest report for a specific host (FQDN)

    for-cli -q reports --host=host.example.com

### Get full lists

#### Retrieve a list of Facts

    for-cli -q facts

#### Retrieve a list of Operatingsystems

    for-cli -q os

#### Retrieve a list of Hosts

    for-cli -q hosts

#### Retrieve a list of Hostsgroups

    for-cli -q hostgroups

#### Retrieve a list of all puppet certificates 

    for-cli -q ca

### Post requests

#### Trigger puppet run / kick on a specific host (FQDN)

    for-cli -q run --host=host.example.com	
