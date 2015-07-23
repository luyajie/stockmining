#chartapi.finance.yahoo.com/instrument/1.0/AAPL/chartdata;type=quote;range=1y/csv
import urllib2
import time
import datetime

#stockToPull = 'NFLX','GOOG','TSLA','AAPL','AMZN','FB','MSFT','EBAY'
stockToPull = 'AAPL','EBAY'

def pullDailyData(stock):
    try:
        fileLine = 'dataDaily/'+stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=3y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            #print splitLine
            if len(splitLine) == 6:
                #print splitLine
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite = eachLine + '\n'
                    #print lineToWrite
                    saveFile.write(lineToWrite)

        print 'Pulled',stock
        print 'sleeping'
        time.sleep(0.1)

    except Exception,e:
        print 'main loop', str(e)

def pullIntradayData(stock):
    try:
        print 'Currently pulling',stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        saveFileName = 'dataIntra/'+stock+'.txt'

        try:
            readExistingData = open(saveFileName,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = mostRecentLine.split(',')[0]

        except:
            lastUnix = 0

        saveFile = open(saveFileName, 'a')
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine) == 6:
                    if int(splitLine[0]) > lastUnix:
                        lineToWrite = eachLine + '\n'
                        saveFile.write(lineToWrite)

        print 'pulled',stock
        print 'sleeping....'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

    except Exception,e:
        print 'main loop', str(e)

for eachStock in stockToPull:
    pullDailyData(eachStock)
    #pullIntradayData(eachStock)

        
