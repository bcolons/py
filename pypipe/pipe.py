#!/usr/bin/env python3
import sys,re
r = re.compile('^([\s]*)(.*)$') # \g<1> is leading whitespace, \g<2> is rest of line
i = int(sys.argv[1]) # prepend i tabs to line
p = ' ' * 4 * i 
for line in sys.stdin :
           sys.stdout.write(r.sub(f'{p}\g<1>\g<2>',line))
