import sys

with open(sys.argv[1], 'r') as fd:
    with open('/dev/tty1', 'w') as fdo:
        o=fd.read() 
        fdo.write(o)
