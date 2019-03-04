from subprocess import PIPE, Popen
from enum import Enum

RC = Enum('OK', 'ERROR', 'TIMEOUT')


class LocalSess(object):

    def __init__(self):
        self.cmd = None

    def connect(self):
        pass

    def close(self):
        pass

    def send(self, cmd):
        self.cmd = cmd

    sendline = send

    def expect(self, seps=None, timeout=-1):
        process = Popen(args=self.cmd, stdout=PIPE, shell=True)
        rsp = process.communicate()[0]
        return rsp



    def __str__(self):
        return self.__class__.__name__

    __repr__ = __str__


