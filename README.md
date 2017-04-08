# myCustomLog
Simple stupid Wrapper class of python logger.  
This will make log easier plus some customized functions that work with extra modules like fbchat.  

# How to install
```
1. clone this repository into your computer
2. python setup.py install
3. done
```

# Example
```
>>> from myCustomLog import myCustomLog
>>> myLog = myCustomLog("testApp","log/")
>>> myLog.log("hello world")
>>> myLog.log("hello sun", logging.ERROR)

log/testApp.log
2017-02-09 23:48:28,070, testApp, INFO, hello world
2017-02-09 23:48:34,863, testApp, ERROR, hello sun
```

# Class Setting and Default value
- appName  
Your application name [REQUIRED]  
- logPath  
Path of the log.  
Default is current working space.  
- level  
Log level. Same as python logger  
Default is logging.INFO  
- format  
Format of log  
Default is '%(asctime)s, %(name)s, %(levelname)s, %(message)s'  
(This is the best, believe me XD)  
- maxKB  
Max size of log. New file will be created when current file exceeds this value. Set maxKB to -1 to ignore file size.  
Default is 10000  
- backupCount  
By default, new files will be created infinitely (max 1000, noone should ever exceeds this amount anyway). If you set this to some number, the log files will be rotated with count no greather than that number. (This config does nothing if setting maxKB to -1)  
Default is -1 (infinite)  
- saveFile  
You might not want a log but a simple save data file, set path here. You can save your data as simple as below example (warning, overwrite if append=0)  
Default is None  
```
myLog.saveData("myCurrentData") # overwrite old file
myLog.saveData("myCurrentData", append=1) # append to the file
```

# Author
Bankde
