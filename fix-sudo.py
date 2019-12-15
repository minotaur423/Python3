#!/usr/bin/env python

import os
import stat
import socket
import shutil

def reinstall_function():
    shutil.copy('/etc/sudoers', '/etc/sudoers.bak')
    os.system('sudo yum -y reinstall sudo')

HOSTNAME=os.getenv('HOSTNAME')
print('------------------------------')
print(HOSTNAME)
print('------------------------------', end='\n')
STAT=os.stat('/etc/sudoers').st_mode

if oct(STAT) != '0o100440':
    print("Reinstalling sudo, since permissions were altered!")
    reinstall_function()
else:
    print('The sudo file permissions are correct. No changes required.', end='\n\n')

f = open('/etc/sudoers', 'r')
try:
    line = f.readline()
    while line:
        if 'root' in line or 'wheel' in line:
            pass
        else:
            if '\tALL\n' in line or ' ALL\n' in line or 'NOPASSWD: ALL' in line:
                print(line)
            else:
                pass
        line = f.readline()
finally:
    f.close()
