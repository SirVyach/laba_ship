import matplotlib.pyplot as plt
import math

M=2150
m=200
g=1.62
a_m=29.43
V_m=3
U=3660
a=0
t=0
erg=0
H = float(input ('Введите H = '))
V = float(input ('Введите V0 = '))
Y = []
T = []

V_ex = V
V = -1*V

#print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', g, 'Расход = ', 0, 'm = ', m)

while V < V_ex:
    V=V+g*0.1
    t += 0.1
    H = H - V*0.1
    #print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', g, 'Расход = ', 0, 'm = ', m)
    Y.append (H)
    T.append (t)
    

if H<=115:
#    print (t, V, H, a, M)
    while V >= V_m:
        a=28
        del_m = M*(28+g)/U
        V=V-a*0.1
        t += 0.1
        H = H - V*0.1
        M = M - del_m*0.1
        m = m - del_m*0.1
        Y.append (H*2)
        T.append (t)
        #print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', a, 'Расход = ', del_m, 'm = ', m)
    if V<2.5:
        while V < 2.5:
            t += 0.1
            H = H - V*0.1
            V = V + g*0.1
            Y.append (t**0.5)
            T.append (t)
            #print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', g, 'Расход = ', del_m, 'm = ', m)
    while H>0:
        del_m = M*g/U
        M = M - del_m*0.1
        m = m - del_m*0.1
        H = H - V*0.1
        t += 0.1
        Y.append (H+t)
        T.append (t)
        #print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', 0, 'Расход = ', del_m, 'm = ', m)
else:

        
    if H <= 1500:
        erg = int(H//500 + 1)
        del_m = (M*(V*V - 9)/(0.6*H) + M*g)/U
    elif H <= 2500:
        erg = int(H//500)
        del_m = (M*(V*V - 9)/(0.2*H) + M*g)/U
    elif H <= 3500:
        erg = int(H//500-1)
        del_m = (M*(V*V - 9)/(0.005*H) + M*g)/U


    print(erg)

    while V >= V_m:
        if H == 0:
            break
        a=28
        del_m = M*(28+g)/U
        V=V-a*0.1
        t += 0.1
        H = H - V*0.1
        M = M - del_m*0.1
        m = m - del_m*0.1
        Y.append (H+t*(math.sinh(1/H)*2.7)**4)
        T.append (t)
#        print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', a, 'Расход = ', del_m, 'm = ', m)

    for i in range (1,erg+1):

        H_ex = H

        while H >= H_ex/2:
            t += 0.1
            V = V + 0.1*g
            H = H - 0.1*V
            Y.append (H+t*(math.sin(H)*2.7)**4)
            T.append (t)
#            print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', g, 'Расход = ', 0, 'm = ', m)

        while V >= V_m:
            if H == 0:
                break
            a=28
            del_m = M*(28+g)/U
            V=V-a*0.1
            t += 0.1
            H = H - V*0.1
            M = M - del_m*0.1
            m = m - del_m*0.1
            Y.append (H+t*(math.sin(H)*2.7)**4)
            T.append (t)
#            print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', a, 'Расход = ', del_m, 'm = ', m)
            
        if V<2.5:
            while V < 2.5:
                t += 0.1
                H = H - V*0.1
                V = V + g*0.1
                Y.append (H-t*2)
                T.append (t)
#                print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', g, 'Расход = ', 0, 'm = ', m)
     
    while H>0:
        del_m = M*g/U
        M = M - del_m*0.1
        m = m - del_m*0.1
        H = H - V*0.1
        t += 0.1
        Y.append (H+t/H)
        T.append (t)
#        print ('t = ', t, 'V = ', V, 'H = ', H, 'a = ', 0, 'Расход = ', del_m, 'm = ', m)

print ("Landing completed successfully")

plt.plot (T, Y)
plt.grid()
plt.show()
    
