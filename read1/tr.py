import os
import subprocess
#os.system('tr a-z A-Z') # deprecated/obsolete way, use following:
subprocess.call('tr a-z A-Z',shell=True)
