#! /usr/bin/env python

### @par Copyright:
### Copyright (c) by ScaleFlux, Inc.
###
### ALL RIGHTS RESERVED. These coded instructions and program statements are
### copyrighted works and confidential proprietary information of ScaleFlux, Inc.
### They may not be modified, copied, reproduced, distributed, or disclosed to
### third parties in any manner, medium, or form, in whole or in part.
###
### @par Description:
### The Description of this file.

import os.path
import logging.config
from dlogging import filehandler
import inspect

# _ variable
_LoggerInit = False

# 2 empty lines between top-level funcs and classes

# added by cliicy.luo 20190227 start
def PrintFrame():
  callerframerecord = inspect.stack()[1]    # 0 represents this line
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  return '{0}{1}'.format('code line: ', info.lineno)                      # __LINE__     -> 13
# added by cliicy.luo 20190227 end


def getLogger(name):
    # logging.config.fileConfig('cfg.ini')
    logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s')
    # handler = filehandler.FileHandler()
    # handler.setLevel(logging.INFO)
    return logging.getLogger(name)


if __name__ == '__main__':

    logger = getLogger('MyLogger1')
    ss1 = '{0} {1}'.format("INFO message1", PrintFrame())
    logger.info(ss1)

    logger2 = getLogger('MyLogger2')
    ss2 = '{0} {1}'.format("INFO message2", PrintFrame())
    logger2.info(ss2)
