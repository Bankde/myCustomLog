#!/usr/bin/python

import logging
import logging.handlers
import os
import datetime

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

    # read config file method
    # config is in "key value" format
    @staticmethod
    def readConfig(configFile, confList=None):
        if confList == None:
            confList = {}
        with open(configFile, "r") as conf:
            for line in conf:
                sline = line.strip()
                if len(sline) == 0 or sline[0] == '#':
                    continue
                s = sline.split()
                assert(len(s) == 2)
                confList[s[0]] = s[1]
        return confList

    def __init__(self, appName, logPath=".", saveFile=None, level=logging.INFO, format='%(asctime)s, %(name)s, %(levelname)s, %(message)s', maxKB=10000, backupCount=-1):
        self.logger = logging.getLogger(appName)
        self.logger.setLevel(level)

        if not logPath == "" and not logPath[-1] == "/":
            logPath = logPath + "/"

        self.logFile = logPath + appName + '.log'
        self.maxBytes = (maxKB*1024)
        self.backupCount = backupCount
        self.logLevel = level
        self.logFormat = format

        self.setFileHandler()

        # save file, make sure directory exists
        self.saveFile = saveFile

    def setFileHandler(self):
        # create file handler
        if self.maxBytes < 0:
            fh = logging.FileHandler(self.logFile)
        else:
            if self.backupCount == -1:
                fh = logging.handlers.RotatingFileHandler(self.logFile, maxBytes=self.maxBytes, backupCount=1000)
            else:
                fh = logging.handlers.RotatingFileHandler(self.logFile, maxBytes=self.maxBytes, backupCount=self.backupCount)
        
        fh.setLevel(self.logLevel)
        # create formatter and add to file handler
        formatter = logging.Formatter(self.logFormat)
        fh.setFormatter(formatter)
        # add file handler to logger (and remove old handler, if exists)
        self.logger.handlers = []
        self.logger.addHandler(fh)


    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def logAndPrint(self, message, level=logging.INFO):
        self.log(message, level)
        print message 

    def logAll(self, message, level=logging.INFO):
        self.log(message, level)
        print message

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
