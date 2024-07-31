import pipes
t = pipes.Template()
t.append('bc -l', '--')
f = t.open('pipefile', 'w') # create a file, enable fd.write(..)
f.write('3+4\n')
f.close()
print(open('pipefile').read())
