import sys 

class star:
    """Demo for opening a list of files given as commandline args.
    Last byte of '10' is EOF for text files.
    Other Errors are caught and displayed."""
for filename  in sys.argv:
    try:
        with open(filename,'b+r') as f: # read as bytes
            o=f.read()
            print('name: '+ filename+' last two bytes:--'+ str(o[-2])+ '--,--'+ str(o[-1])+'--')
    except IsADirectoryError:
        print('directory! err: '+filename) 
    except UnicodeDecodeError:
        print('unicode dec err: '+filename) 
    except PermissionError:
        print('permish err: '+filename)
