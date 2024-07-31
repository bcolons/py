import sys 
fdtt2=open('/proc/134/fd/0','wb')
fdr=open('eof','rb')
fdw=open('ab','wb')
fdtt2.write(b'2+3')
b=fdr.read(1)
fdtt2.write(b)
