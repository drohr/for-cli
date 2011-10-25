## for-cli

Simple python CLI to interact with the REST-API for foreman. http://theforeman.org/

Make sure to change the default username/password and baseurl for your foreman installation

### Query for facts

#### Get all hosts and values for a specific fact (kernelversion)

    for-cli -f facts kernelversion

#### Get all facts and values for a specific host (FQDN)

    for-cli -f facts --host=host.example.com

### Query for status

#### System status (result ok/failed, database lag in miliseconds)

    for-cli -f status

#### Summary statistcs (total hosts, active hosts, hosts in error etc)

    for-cli -f dashboard

### Query for operatingsystems

#### Retrieve a list of Operatingsystems

    for-cli -f os
