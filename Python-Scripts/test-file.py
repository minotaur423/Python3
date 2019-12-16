#!/bin/python

with open('/etc/sudoers') as f:
    line = f.readline()
    while line:
        if 'root' in line or 'wheel' in line:
            pass
        else:
            if ' ALL\n' in line or 'NOPASSWD:ALL' in line:
                print(line)
            else:
                pass
        line = f.readline()