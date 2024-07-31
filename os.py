import os
# newco
unos=os.uname()
ost=os.times()
print('type(unos.uname()) '+str(type(os.uname())))
[print(i) for i in [unos.sysname,unos.nodename,unos.version,unos.release,unos.machine, os.confstr_names,os.cpu_count(),os.getloadavg(),os.sysconf_names,os.curdir,os.pardir,os.urandom(9),ost.user,ost.system,ost.children_user,ost.children_system,ost.elapsed]]
