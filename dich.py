import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random
from cmath import sqrt

def init():
    return []

n = 100

# def colorlist():

def validation(cord):
    while cord > 2:
        cord -= 2
    while cord < 0:
        cord +=2
    return cord


def getx(i):
    b = []
    for j in range(n):
        q = a[j][0] + 0.005 * a[j][2]  # x[i] = x[i-1]+vx/200
        q = validation(q)
        a[j][0] = q
        b.append(q)
    return b


def gety(i):
    b = []
    for j in range(n):
        q = a[j][1] + 0.005 * a[j][3]
        q = validation(q)
        a[j][1] = q
        b.append(q)
    return b


def dist(f, s):
    return (f[0] - s[0]) ** 2 + (f[1] - s[1]) ** 2


def getcolor():
    b = []
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if dist([ a[j][0], a[j][1] ], [ a[k][0], a[k][1] ]) < 0.05 ** 2 and a[j][4] != a[k][4]:
                a[j][4] = 'r'
                a[k][4] = 'r'
                
    for j in range(n):
        b.append(a[j][4])
        
    return b
        

def animate(i):
    x = getx(i)
    y = gety(i)
    clr = getcolor()
    bx, rx, by, ry = [[], [], [], []]
    
    for i in range(n):
        if clr[i] == 'b':
            bx.append(x[i])
            by.append(y[i])
        else:
            rx.append(x[i])
            ry.append(y[i])
    
    return ax.plot(bx, by, 'bs', rx, ry, 'ro', antialiased=False, ms=3)


#np.random.seed(0)
#buf = -1 + 2 * np.random.random((100, 4))# x y vx vy

a = []

for i in range(n):
    a.append([])
    for j in range(2):
        a[i].append(random.uniform(0, 2))
    for j in range(2):
        a[i].append(-1 + random.uniform(0, 2))
    a[i].append('b')

a[0][4] = 'r'

#print(a)

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(0, 2))
#slozhna = ax.plot([], [], 'b', [], [], 'r', 'o', ms=3)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
plt.show()
