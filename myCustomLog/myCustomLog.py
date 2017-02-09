#!/usr/bin/python

import logging
import os
import datetime

try:
    import fbchat
    en_fbchat = 1
except ImportError:
    en_fbchat = 0

# static var on log level
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

class myCustomLog:

    # class var on log level
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    def __init__(self, appName, logPath=".", saveFile=None, level=logging.INFO, format='%(asctime)s, %(name)s, %(levelname)s, %(message)s', maxFileSizeKB=10000, fileRoundRobin=-1, fbchatClient=None):
        self.logger = logging.getLogger(appName)
        self.logger.setLevel(level)

        if not logPath == "" and not logPath[-1] == "/":
            logPath = logPath + "/"

        self.logFile = logPath + appName + '.log'
        self.maxFileSizeKB = maxFileSizeKB
        self.fileRoundRobin = fileRoundRobin
        # check for existing file
        self.logFileSizeExceedAction()

        # create file handler
        fh = logging.FileHandler(self.logFile)
        fh.setLevel(level)
        # create formatter and add to file handler
        formatter = logging.Formatter(format)
        fh.setFormatter(formatter)
        # add file handler to logger (and remove old handler, if exists)
        self.logger.handlers = []
        self.logger.addHandler(fh)

        # save file, make sure directory exists
        self.saveFile = saveFile

        # if we use fbchat in log
        if en_fbchat and fbchatClient:
            self.client = fbchatClient

    if en_fbchat:
        def setFbChatClient(self, fbchatClient):
            self.client = fbchatClient

    def fileIncreaseVer(self, rename_file, run=1):
        if not self.fileRoundRobin == -1 and run > self.fileRoundRobin:
            return False
        newFile = self.logFile + ".%d" % (run)
        if os.path.isfile(newFile):
            run += 1
            self.fileIncreaseVer(newFile, run)
        os.rename(rename_file, newFile) 
        return True

    def logFileSizeExceedAction(self):
        if self.maxFileSizeKB < 0:
            return False
        if os.path.isfile(self.logFile) and (os.path.getsize(self.logFile)/1000) >= self.maxFileSizeKB:
            # old file exists and exceed the size, change its name
            return self.fileIncreaseVer(self.logFile)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def chat(self, message, uid):
        if en_fbchat == 1:
            # check if uid is array
            if hasattr(uid, '__iter__'):
                for i in uid:
                    sent = self.client.send(i, message)
                    if not sent:
                        self.logAndPrint("fbchat sent error\r\n", level=logging.ERROR)
            else:
                sent = self.client.send(uid, message)
                if not sent:
                    self.logAndPrint("fbchat sent error\r\n", level=logging.ERROR)
        else:
            self.logAndPrint("fbchat not enabled, please install fbchat first\r\n\t$ pip install fbchat")

    def logAndPrint(self, message, level=logging.INFO):
        self.log(message, level)
        print message 

    def logAndChat(self, message, uid, level=logging.INFO):
        self.log(message, level)
        self.chat(message, uid)

    def logAll(self, message, uid, level=logging.INFO):
        self.log(message, level)
        print message
        self.chat(message, uid)

    def saveData(self, data, append=0):
        try:
            if append == 0:
                f = open(self.saveFile, 'w+')
            else:
                f = open(self.saveFile, 'a+')
            f.write(str(data))
            f.close()
            return True
        except:
            return False

    def loadData(self):
        if os.path.isfile(self.saveFile):
            f = open(self.saveFile, 'r')
            s = [line.strip() for line in f]
            return s
        else:
            return None
