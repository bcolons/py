if(__name__=='__main__'):
    with open('enum.py', 'r') as f:
        alll=f.readline() # list of characters in first line
        for line in alll:
            print(line)
    with open('enum.py', 'r') as f:
        alll=f.readlines() # list of lines in file 
        for line in alll:
            print(line)
    with open('enum.py', 'r') as f:
        alll=f.read() # list of characters in file 
        for line in alll:
            print(line,end='')
