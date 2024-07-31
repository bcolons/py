import pipes
t = pipes.Template()
t.append('tr a-z A-Z', '--')
f = t.open('pipefile', 'w') # create a file, enable fd.write(..)
f.write('hello world')
f.close()
print(open('pipefile').read())
