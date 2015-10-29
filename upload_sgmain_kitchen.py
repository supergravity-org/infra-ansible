#!/usr/bin/env python
import yaml, subprocess

fd = open('.kitchen/web-ubuntu-1404.yml')
data = yaml.load(fd)
print(data)

do = [
    'rsync', '-avz',
    '--chown', 'supergravity_main:www-data',
    '--exclude', 'local.py',
    '-e',
      'ssh -i ' +  data['ssh_key'] +
      ' -o StrictHostKeyChecking=no ' +
      '-p '+ data['port'],
    '--rsync-path="/usr/bin/sudo /usr/bin/rsync"',
    'supergravity_main', data['username'] + '@' + data['hostname'] + ':/srv/wagtail_supergravity_main/'

]
print(do)
print(" ".join(do))
subprocess.call(do)
