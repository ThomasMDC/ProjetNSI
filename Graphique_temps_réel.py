import cryptocompare
import datetime
from pylab import *
from matplotlib import animation

count = 0

x = []
x.append(count)
y = []
b = cryptocompare.get_price('BTC')
for i in b.values():
    for j in i.values():
        y.append(j)
        
figure("BTC")
plot(x, y, label='price', color = 'r')
xlabel("Temps")
legend()

def draw_graph(i):
    global count
    count += 1
    x.append(count)
    b = cryptocompare.get_price('BTC')
    for i in b.values():
        for j in i.values():
            y.append(j)
    plot(x, y, label='open', color = "r")
    
anima = animation.FuncAnimation(gcf(), draw_graph, interval=100)
show()