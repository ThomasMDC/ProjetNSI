import time
import pandas as pd
import cryptocompare
import matplotlib.pyplot as plt

def SAR(data,acc=0.2):
    liste_close=list(data["close"])
    liste_high=list(data["high"])
    liste_low=list(data["low"])
    sar=[liste_close[0],liste_close[1]]
    conseil=[]
    if liste_close[0]<liste_close[1]:
        up=True
    else:
        up=False
    for i in range(2,1441):
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
            conseil.append((i,up))
    return conseil

# True : Achat
# False: Vente