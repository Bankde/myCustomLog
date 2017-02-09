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
>>> myLog = myCustomLog("testApp","test/")
>>> myLog.log("hello world")
>>> myLog.log("hello sun")

testApp.log
2017-02-09 23:48:28,070, testApp, INFO, hello world
2017-02-09 23:48:34,863, testApp, INFO, hello sun
```

# Class Setting and Default value
- maxFileSizeKB=10000  
New file will be created when current file exceeds 10MB (when init the class, I haven't checked when writing yet, too lazy XD)  
- fileRoundRobin=-1  
The file will be created infinitely. If you set fileRoundRobin to some number, the number of log.num file will be no more than that number. Older log file will be deleted.  
- saveFile=None  
You might not want a log but a simple save data file, set path here. You can save your data as simple as below example (warning, overwrite if append=0)  
```
myLog.saveData("myCurrentData") # overwrite old file
myLog.saveData("myCurrentData", append=1) # append to the file
```
- level=logging.INFO  
Same as python logger  
- format='%(asctime)s, %(name)s, %(levelname)s, %(message)s'  
This is the best, believe me XD  
- fbchatClient=None  
If you happen to also use fbchat (https://github.com/carpedm20/fbchat), initialize somewhere then throw into this class. So you can lazily call fbchat together with log.  
```
myLog.logAndChat('yourMessage', uid='YourUID')
```

# Author
Bankde
