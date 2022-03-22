import cryptocompare
import time
import matplotlib.pyplot as plt
import os
import datetime
os.environ['CRYPTOCOMPARE_API_KEY'] = '0e7dcff8fd78bdb476138ad0462ff0428facba9ebae506a5b1e02cd23eaf3806'
date2 = datetime.datetime.now()
date1 = date2-3600*24*6
v1=0
v2=0
while date<date2:
    x=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    Infos = cryptocompare.get_historical_price_minute('BTC', 'EUR', limit=60, exchange='CCCAGG', toTs=date)
    i=0
    dateInter=date+3600
    while date<dateInter:
        info = Infos[i]
        x.append(date)
        y1.append(info["open"])
        y2.append(info["close"])
        y3.append(info["high"])
        y4.append(info["low"])
        i+=1
        date+=60
    plt.figure()
    plt.plot(x, y1, c="green")
    plt.plot(x, y2, c="red")
    plt.plot(x, y3, c="yellow")
    plt.plot(x, y4, c="blue")
    prix1=cryptocompare.get_historical_price_minute('BTC', 'EUR', limit=1, exchange='CCCAGG', toTs=date)[1]["low"]
    prix2=cryptocompare.get_historical_price_minute('BTC', 'EUR', limit=1, exchange='CCCAGG', toTs=date+600)[1]["low"]
    if prix1<prix2:
        plt.savefig("Graphes/0_"+str(v1)+".jpg")
        v1+=1
    else:
        plt.savefig("Graphes/1_"+str(v2)+".jpg")
        v2+=1
    plt.close()