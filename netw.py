# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
import os
from dlogging import logger, filehandler
from sub_comu import LocalSess


logger = logger.getLogger(__name__)
logger.addHandler(filehandler.FileHandler('ping_logs'))

list = ["baidu"]
# list = ["taobao","jd","baidu"]

i = 0
while True:
    str = "ping -c 5 www."
    command = str+list[i]+".com"
    # ret = os.system(strlist[i])
    # r = os.popen(command)
    # info = r.readlines()
    rc = 0
    rsp = ''
    ret_msg = ''
    sess = LocalSess()

    sess.connect()
    sess.send(command)
    ret = sess.expect()
    logger.info("****     %s", ret)

