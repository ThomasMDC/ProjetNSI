import time
import pandas as pd
import cryptocompare
import matplotlib.pyplot as plt

#importation data
data=cryptocompare.get_historical_price_minute("btc",currency="eur",limit=240)
pd_data=pd.DataFrame(data,columns=['time', 'open', 'high', 'low', 'close', 'volumeto'])
pd_data.set_index("time",inplace=True)
liste_close=list(pd_data["close"])

#création Parabolique SAR
def SAR(data,acc=0.02):
    liste_close=list(data["close"])
    liste_high=list(data["high"])
    liste_low=list(data["low"])
    sar=[liste_close[0],liste_close[1]]
    if liste_close[0]<liste_close[1]:
        up=True
    else:
        up=False
    for i in range(2,241):
        if up==True:
            sar.append(float(sar[i-1]+acc*(liste_high[i-1]-sar[i-1])))
        else:
            sar.append(float(sar[i-1]+acc*(liste_low[i-1]-sar[i-1])))
        if sar[i]<liste_high[i] and sar[i]>liste_low[i]:
            sar.pop()
            up=not(up)
            if up==True:
                sar.append(float(sar[i-1]+acc*(liste_high[i-1]-sar[i-1])))
            else:
                sar.append(float(sar[i-1]+acc*(liste_low[i-1]-sar[i-1])))
            print(i,up)
    return sar

#Affichage du graphique
pd_data['SAR']=SAR(pd_data,0.2)
plt.style.use('fast')
pd_data[["close",'SAR']].plot(figsize=(10,5))
plt.grid()
plt.show()
