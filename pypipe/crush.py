import sys,re
i=1
if len(sys.argv) > 1:
    i = int(sys.argv[0])
p = '    ' * i 
r = re.compile(f'^({p})(\s*)(.*)$')
for line in sys.stdin :
        sys.stdout.write(r.sub(f'\g<2>\g<3>',line))
        if True:
            pass
