#!/usr/bin/env python
# foreman cli <david@rohr.se>

import urllib2, base64, json, sys
from optparse import OptionParser

def main():

    # basic settings
    username = 'foreman' # or use sys.argv[2]
    password = 'foreman' # or use sys.argv[3]
    baseurl = 'http://foreman.example.com'

    # if no input, show some love
    usage = "usage: %prog [options] arg1 arg2"
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: for-cli -h\n')
        sys.exit(1)

    # optparse values
    parser = OptionParser(usage="%prog [option] arg", version="%prog 0.5")
    parser.add_option("--function",
        metavar="FUNCTION", dest="function", default=False, action="store", help="Dump info for Function")
    parser.add_option("--host",
        metavar="HOST", dest="host", default=False, action="store", help="Dump info for HOST")
    parser.add_option("--verbose",
        metavar="DEBUG", dest="verbose", action="store_true", help="Prints some debug stuff")
    (options, args) = parser.parse_args()

    # debug stuff   
    if options.verbose:
        print 'ARGV      :', sys.argv[1:] 
        print 'FUNCTION  :', options.function
        print 'HOST      :', options.host
        print 'REMAINING :', args 

    # ugly function switch
    if options.function:
        function = options.function
        # facts
        if function == 'facts':
            fact = sys.argv[2] 
            url = "%s/facts/%s/values" % (baseurl, fact)
            print("listing hosts with %s\n" % (fact))
            if options.host:
                host = options.host
                url = "%s/hosts/%s/facts" % (baseurl, host)
                print("listing facts for %s\n" % (host))
        if function == 'status':
            url = "%s/%s" % (baseurl, function)
            print("getting status")
    else:
        sys.exit(0)
   
    # send request with urllib2
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-Type", "application/json")
    htmlFile = urllib2.urlopen(request)
    # parse it with json
    htmlData = json.load(htmlFile)
    print json.dumps(htmlData, sort_keys=True, indent=1)
    htmlFile.close()

if __name__ == '__main__':
    main()
