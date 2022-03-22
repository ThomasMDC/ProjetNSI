import cryptocompare
import time
import datetime
import matplotlib.pyplot as plt
import os
os.environ['CRYPTOCOMPARE_API_KEY'] = '0e7dcff8fd78bdb476138ad0462ff0428facba9ebae506a5b1e02cd23eaf3806'
x=[]
y1=[]
y2=[]
y3=[]
y4=[]
Infos = cryptocompare.get_historical_price_minute('BTC', 'EUR', limit=60, exchange='CCCAGG', toTs=datetime.datetime.now())
for info in Infos:
    x.append(info["time"])
    y1.append(info["open"])
    y2.append(info["close"])
    y3.append(info["high"])
    y4.append(info["low"])
plt.figure()
plt.plot(x, y1, c="green")
plt.plot(x, y2, c="red")
plt.plot(x, y3, c="yellow")
plt.plot(x, y4, c="blue")
plt.savefig("GraphesVictor/"+str(x[-1])+".jpg")
plt.close()