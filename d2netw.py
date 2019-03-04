# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
import os
import datetime
import io

dtime   = datetime.datetime.now().strftime("%y%m%d_%H%M")
file = dtime + '.txt'
str = "sudo ping -c 5 www.baidu.com"
dir = '/var/www/html/app-auto/ping_logs/'
path = dir+file
command = str+' >> '+path
if not os.path.exists(dir):
    os.mkdir(dir)
if not os.path.exists(path):
    f = open(path, 'w')
    f.close()

i = 0
while True:
    os.system(command)
