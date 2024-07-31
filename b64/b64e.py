import base64
import sys

with open(sys.argv[1],'rb') as fdi:
    bites=fdi.read()
    with open(sys.argv[2],'wb') as fdo:
       base64.encode(fdi,fdo) #no output in fdo
    #print(base64.b64encode(bites)) #complains about input.read(MAX...
