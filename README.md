## Python CLI for Foremans REST-API

Simple python CLI to interact with foremans REST-API.

Make sure to change the default username/password and baseurl for your foreman installation

### Query for facts

#### Get all hosts and values for a specific fact (kernelversion)

    for-cli -f facts kernelversion

#### Get all facts and values for a specific host (host.example.com)

    for-cli -f facts --host=host.example.com

### Query for status

#### Get status information from foreman

    for-cli -f status
