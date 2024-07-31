'Shows blocking fd.read(1) behavior for two alternating blocked on input "read(1byte)" calls, ttys echoing chars to a third (good model for asynch/concur/multithread demos...)'
fdr=open('/dev/tty2','r')
fdr1=open('/dev/tty3','r')

fdw=open('/dev/tty1','w')
fdw1=open('/dev/tty1','w')
while True:
    b=fdr.read(1)
    print(b+b)
    #fdw1.write(b+b)
    bb=fdr1.read(1)
    print(bb+bb)    
    #fdw.write(b+b)
