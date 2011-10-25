## Python CLI for Foremans REST-API

### Query for facts

#### Get all hosts and values for a specific fact (kernelversion)

    for-cli -f facts kernelversion

#### Get all facts and values for a specific host (host.example.com)

    for-cli -f facts --host=host.example.com

### Query for status

#### Get status information from foreman

    for-cli -f status
