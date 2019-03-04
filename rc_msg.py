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

from enum import enum

RC = enum('OK', 'ERROR', 'TIMEOUT', 'WARNING', 'MISMATCH', 'NOT_YET', 'CONTINUE', 'NOT_FOUND')


class RcMsg(object):
    ''' Return code and its message '''

    def __init__(self, rc = RC.OK, msg = None):
        self.rc = rc
        self.msg = msg

    def setRC(self, rc, msg=None):
        self.rc = rc
        self.msg = msg

    def __str__(self):
        if self.msg and self.msg != "":
            return "%s-'%s'" % (self.rc, self.msg)
        else:
            return self.rc.__repr__()

    __repr__ = __str__

if __name__ == '__main__':
    rcMsg = RcMsg(RC.ERROR, "has error")
    print rcMsg

