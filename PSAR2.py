import pandas as pd
import cryptocompare
import numpy
import matplotlib.pyplot as plt

data=cryptocompare.get_historical_price_minute("btc",currency="eur",limit=1440)
pd_data=pd.DataFrame(data,columns=['time', 'open', 'high', 'low', 'close', 'volumeto'])
#pd_data.set_index("time",inplace=True)



def sar(s, af=0.02, amax=0.2):
    high, low = s.high, s.low
    sig0, xpt0, af0 = True, high[0], af
    sar = [low[0] - (high - low).std()]
    for i in range(1, len(s)):
        sig1, xpt1, af1 = sig0, xpt0, af0
        lmin = min(low[i - 1], low[i])
        lmax = max(high[i - 1], high[i])
        if sig1:
            sig0 = low[i] > sar[-1]
            xpt0 = max(lmax, xpt1)
        else:
            sig0 = high[i] >= sar[-1]
            xpt0 = min(lmin, xpt1)
        if sig0 == sig1:
            sari = sar[-1] + (xpt1 - sar[-1])*af1
            af0 = min(amax, af1 + af)
            if sig0:
                af0 = af0 if xpt0 > xpt1 else af1
                sari = min(sari, lmin)
            else:
                af0 = af0 if xpt0 < xpt1 else af1
                sari = max(sari, lmax)
        else:
            af0 = af
            sari = xpt0
        sar.append(sari)
    return sar


sar=sar(pd_data)
"""
#Affichage parabolique SAR :
pd_data['SAR']=sar
plt.style.use('fast')
pd_data[["close",'SAR']].plot(figsize=(10,5))
plt.grid()
plt.show()
"""
order_temp=[0 for i in range(1441)]

def flip_signal(close, sar, order):
    for i in range(len(close)):
        try:
            if sar[i] <= close[i] and sar[i-1] > close[i-1]:
                order[i] = 1
            elif sar[i] >= close[i] and sar[i-1] < close[i-1]:
                order[i] = -1
            else:
                continue
        except IndexError:
            pass
    return order

order=flip_signal(list(pd_data.close),sar,order_temp)
"""
for i in range(len(order)):
    if order[i]!=0:
        print(order[i])
"""

def simul(close,order,initial,mise):
    pm=initial
    valeur_b=0
    achat=False
    for i in range(len(order)):
        if order[i]==1:
            pm-=mise
            valeur_b=close[i]
            achat=True
        elif order[i]==-1:
            if achat:
                pm += (mise / valeur_b) * close[i]
                valeur_b=0
                achat=False
    if valeur_b!=0:
        pm+=mise
    return pm

print(simul(pd_data.close,order,1000,100))