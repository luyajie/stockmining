import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
# change font of the labels
import matplotlib
matplotlib.rcParams.update({'font.size': 9})
# candle stick
from matplotlib.finance import candlestick_ochl

stocks = 'AAPL',

def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas



def graphData(stock):
    try:
        stockFile = 'dataDaily/'+stock+'.txt'

        date,closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,
                                                         converters={0:mdates.strpdate2num('%Y%m%d')})

        fig = plt.figure()
        
        # subplot 1: price
        #ax1 = plt.subplot(2,1,1)#(2,3,6), 2X3, and at place 6
        ax1 = plt.subplot2grid((5,4),(0,0),rowspan=4,colspan=4)
        
        ax1.plot(date,openp)
        ax1.plot(date,highp)
        ax1.plot(date,lowp)
        ax1.plot(date,closep)
        # label
        #plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.title(stock)

        # set tick label
        plt.setp(ax1.get_xticklabels(),visible=False)

        #grid
        ax1.grid(True)
        
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        # subplot 2: volume
        #ax2 = plt.subplot(2,1,2,sharex=ax1) #share axis, sync the axis
        ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1,rowspan=1,colspan=4)
        # remove y axis tick lable for subplot2
        ax2.axes.yaxis.set_ticklabels([])
        
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        ax2.bar(date,volume)
        ax2.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Volume')

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        #adjust plot spaces
        plt.subplots_adjust(left=.09,bottom=.17,right=.93,top=.93,wspace=.20,hspace=.00)
        
        plt.show()
        fig.savefig('example.png')

    except Exception, e:
        print 'failed main loop',str(e)

def candlestickData(stock,MA1,MA2):
    try:
        stockFile = 'dataDaily/'+stock+'.txt'

        date,closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,
                                                         converters={0:mdates.strpdate2num('%Y%m%d')})

        # use while loop to build candlestick DATA set
        x = 0
        y = len(date)
        candleAr = []
        while x < y:
            appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
            candleAr.append(appendLine)
            x+=1

        # generate moving average
        Av1 = movingaverage(closep, MA1)
        Av2 = movingaverage(closep, MA2)

        SP = len(date[MA2-1:]) # starting point

        #
        label1 = str(MA1)+' SMA'
        label2 = str(MA2)+' SMA'

        #print len(Av1),len(Av2),len(date)
        #print len(date),SP
        #print date[-SP:],Av1[-SP:]
        #time.sleep(5)
        
            
        #fig = plt.figure()
        fig = plt.figure(facecolor='#07000d') # background color
        
        # subplot 1: price
        #ax1 = plt.subplot(2,1,1)#(2,3,6), 2X3, and at place 6
        ax1 = plt.subplot2grid((5,4),(0,0),rowspan=4,colspan=4,axisbg='#07000d')

        # candle stick plot
        # make change to vline in candlestick()
        #candlestick(ax1,candleAr,width=0.8,colorup='#9eff15',colordown='#ff1717')
        candlestick_ochl(ax1,candleAr,width=0.8,colorup='#9eff15',colordown='#ff1717')

        #plot moving average
        ax1.plot(date[-SP:],Av1[-SP:],'#6998ff',label=label1,linewidth=1.5)
        ax1.plot(date[-SP:],Av2[-SP:],'#e1edf9',label=label2,linewidth=1.5)
        #ax1.plot(date[MA1-1:],Av1[:],'#6998ff',label=label1,linewidth=1.5)
        #ax1.plot(date[MA2-1:],Av2[:],'#e1edf9',label=label2,linewidth=1.5)
        
        #
        ax1.yaxis.label.set_color('w')
        ax1.spines['bottom'].set_edgecolor('#5998ff')
        ax1.spines['top'].set_edgecolor('#5998ff')
        ax1.spines['left'].set_edgecolor('#5998ff')
        ax1.spines['right'].set_edgecolor('#5998ff')
        ax1.tick_params(axis='y',colors='w')
        
        # label
        #plt.xlabel('Date')
        plt.ylabel('Price ($)',color='w')
        plt.suptitle(stock,color='w')

        # plot legend
        plt.legend(loc=2,prop={'size':6})

        # fill color
        #volumeMin = volume.min()
        volumeMin = 0

        # set tick label
        plt.setp(ax1.get_xticklabels(),visible=False)

        #grid
        ax1.grid(True,color='w')
        
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        # subplot 2: volume
        #ax2 = plt.subplot(2,1,2,sharex=ax1) #share axis, sync the axis
        ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1,rowspan=1,colspan=4,axisbg='#07000d') # shared axis
        # remove y axis tick lable for subplot2
        ax2.axes.yaxis.set_ticklabels([])
        
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        #
        ax2.yaxis.label.set_color('w')
        ax2.spines['bottom'].set_edgecolor('#5998ff')
        ax2.spines['top'].set_edgecolor('#5998ff')
        ax2.spines['left'].set_edgecolor('#5998ff')
        ax2.spines['right'].set_edgecolor('#5998ff')
        ax2.tick_params(axis='x',colors='w')
        ax2.tick_params(axis='y',colors='w')
        
        #ax2.bar(date,volume)
        ax2.plot(date,volume,'#00ffe8',linewidth=.8)
        ax2.fill_between(date,volumeMin,volume,facecolor='#00ffe8',alpha=.5)
        
        ax2.grid(False)
        plt.xlabel('Date')
        plt.ylabel('Volume')

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        #adjust plot spaces
        plt.subplots_adjust(left=.09,bottom=.17,right=.93,top=.93,wspace=.20,hspace=.00)
        
        plt.show()
        fig.savefig('example.png',facecolor=fig.get_facecolor())

    except Exception, e:
        print 'failed main loop',str(e)
                    
for eachStock in stocks:
    #graphData(eachStock)
    candlestickData(eachStock,12,26)
    #time.sleep(5)
