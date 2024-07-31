import inspect
import contextvars
def foreachwriter(arr,fdo):
    for each in arr:
        fdo.write(str(each))
        fdo.write('\n')
def sumfun():
    f3=open('file3','w')
    foreachwriter( inspect.getmembers(contextvars.copy_context()),f3)
    
with open('file1','w') as f1:
    foreachwriter( inspect.getmembers(contextvars.copy_context()),f1)
f2=open('file2','w')
foreachwriter(inspect.getmembers(contextvars.copy_context()),f2)
sumfun()


