#!/usr/bin/env python3
import sys,re
i=1
out=''
if len(sys.argv) > 2:
    i = int(sys.argv[1])
r = re.compile(f"'")
s = re.compile(f",")
for line in sys.stdin :
    for ch in line:
        if not r.match(ch)and not s.match(ch):
            out+=ch
print(out)
