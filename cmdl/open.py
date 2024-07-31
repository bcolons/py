import sys

with open('newfile','a') as nf:
    nf.write('somestuff...') # append chars/bytes to file
    with open('newfile','r') as nfr:
        fourchars=nfr.read(4) # read 4 chars...
        print(fourchars)
out=sys.stdin.read(4) # blocks until 4 chars+newline
sys.stdout.write('stdo w: '+out+'\n') # writes same 4 chars , equiv to print(..)
with open('/dev/tty2','r') as ttr:
    with open('/dev/tty2','a') as tta: # can have same file open for reading and writing
        tta.write(out) # write the stdin read to remote tty
    fourch=ttr.read(4) # read remote tty input, not 'out' from above; need to enter 5chars to push the 4 asked for
    sys.stdout.write(fourch) #confirm chars appear
"Three somewhat equivalent ways to write data out to terminal: \
    open('/dev/tty1','w') as ttw: # this has benefit of prototyping for actual files w/o the development hassle\
        ttw.write(out); \
    sys.stdout.write(out) \
    print(out) "

"Three somewhat equivalent ways to read data from terminal: \
    open('/dev/tty1','r') as ttr:
        inp=ttr.read(..) # occurs once specified number of bytes has been read (unlike the others) 
    inp=sys.stdin.read(..) # occurs following \n
    inp=input(..) # occurs follwoing \n
