#!/usr/bin/python 

import boto.ec2
from optparse import OptionParser
import base64
import hashlib

def get_connection(region):
    """ Return ec2 connection """
    conn = boto.ec2.connect_to_region(region)
    return conn

def return_keypair(keyfile):
    """ read keypair from file and return tuple keyname and data """
    with open(keyfile, 'r') as file:
      key_data = file.read()
    file.close()
    name = keyfile.split('/')[-1]
    return (name, key_data)

def import_keypair(conn, key_name, key_data):
    """ import key to AWS """
    conn.import_key_pair(key_name, key_data)

def main():
    """ main """
    parser = OptionParser(usage="usage: %prog [options] filename")
    parser.add_option("-r", "--region",
                      dest="region",
                      help="aws region to connect to")
    parser.add_option("-k", "--keyfile",
                      dest="keyfile",
                      help="public key file to upload")
    (options, args) = parser.parse_args()
    conn = get_connection(options.region)
    keyname, key_data = return_keypair(options.keyfile)
    import_keypair(conn, keyname, key_data) 

if __name__ == '__main__':
    main()
