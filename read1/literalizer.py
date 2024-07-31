import sys 
#fdr=open('/dev/tty3','rb')
fdr=open('eof','rb')
fdw=open('ab','wb')
fdw.write(b'3+9\n')
b=fdr.read(1)
fdw.write(b)
