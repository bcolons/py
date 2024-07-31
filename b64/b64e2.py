import base64
import sys

'''Encode first filename arg and write to second filename arg.'''
with open(sys.argv[1],'rb') as fdi:
    with open(sys.argv[2],'wb') as fdo:
        fdo.write(base64.b64encode(fdi.read()))
