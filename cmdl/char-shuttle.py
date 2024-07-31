import sys
'Shows blocking fd.read(1) behavior for two input ttys echoing chars to a third (good model for asynch/concur/multithread demos...)'
file1='file1'
fdr=open('/dev/tty2','r')

fdw=open('/dev/tty1','w')
while True:
    b=fdr.read(1)
    #neither of below really work...
    #sys.stdout.write(b+b)
    fdw.write(b+b)
    fdw.flush()
