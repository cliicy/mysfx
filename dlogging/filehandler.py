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
import logging
import datetime


class FileHandler(logging.FileHandler):

    def __init__(self, filename, mode='a', encoding=None, delay=0):
        # homeDir = os.path.expanduser('~')
        # filename = os.path.join(homeDir,filename)
        filename = os.path.join('/var/www/html/app-auto/',filename)
        dtime    = datetime.datetime.now().strftime("%y%m%d")
        filename = os.path.join(filename, dtime)
        path = os.path.dirname(filename)
        try:
            os.makedirs(path)
        except OSError as exc:
            if not os.path.isdir(path):
                raise
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)


if __name__ == '__main__':
    print FileHandler('<HOME>/<TIME>/aa')
