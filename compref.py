#!/usr/bin/env python3
import sys,re
''' ApatBpat goes to Bpat # Apat (in this case Apat is filename:lineno) '''
#pad r = re.compile('^([\s]*)(.*)$')
r = re.compile('^/usr/lib/python([^:]*):([^:]*):(.*)$')
for line in sys.stdin :
       sys.stdout.write(r.sub('\g<3>                # \g<1>:\g<2>',line))
