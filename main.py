from Parabolique_SAR import SAR 
import time
import pandas as pd
import cryptocompare
import matplotlib.pyplot as plt

#recupération data
data=cryptocompare.get_historical_price_minute("btc",currency="eur",limit=1440)
pd_data=pd.DataFrame(data,columns=['time', 'open', 'high', 'low', 'close', 'volumeto'])
pd_data.set_index("time",inplace=True)
liste_close=list(pd_data["close"])

#test de la stratégie Parabolique SAR
def simul_SAR(initial, mise):
    global pd_data
    liste = SAR(pd_data)
    valeur_b_buy = 0
    for i in liste:
        if i[1] == True:
            initial -= mise
            valeur_b_buy = list(pd_data["close"])[i[0]]
        elif i[1] == False:
            if valeur_b_buy != 0:
                initial += (mise / valeur_b_buy) * list(pd_data["close"])[i[0]]
    return initial

print(simul_SAR(1000,10))