##BACKUP FOR THE CODE IN SA_test2.py
##ADD joint constraints
##Interpolation based on time????

import matplotlib.pyplot as plt
import math
x0=0
y0=0
l1=2384
l2=1462

Xcurrent_pos=2000
Zcurrent_pos=200

Xcurrent_pos1=Xcurrent_pos
Zcurrent_pos1=Zcurrent_pos



w=50
Xtarget_pos=3090
Ztarget_pos=-180
for i in range (w): 

    x=Xcurrent_pos1+((Xtarget_pos-Xcurrent_pos)/w)
    z=Zcurrent_pos1+((Ztarget_pos-Zcurrent_pos)/w)
    Xcurrent_pos1=x
    Zcurrent_pos1=z
    #x=2900+(i*10)
    #z=10-(i*10)
    print(Xcurrent_pos)
    print(Zcurrent_pos)    
    a=math.atan(z/x)
    a_deg=a*(180/math.pi)
    l3=x/(math.cos(a))

    s=math.acos((math.pow(l1,2)+math.pow(l3,2)-math.pow(l2,2))/(2*l1*l3))
    s_deg=(s*(180/math.pi))
    theta1=s_deg+a_deg
    print("SHOULDER ANGLE",theta1)
    rad1=s+a

    o=math.acos((math.pow(l2,2)+math.pow(l3,2)-math.pow(l1,2))/(2*l2*l3))

    e=math.pi-o-s
    e_deg=e*(180/math.pi)
    theta2=(e_deg-180+theta1)
    print("ELBOW ANGLE from base frame",theta2)

    rad2=theta2*math.pi/180

    x1=l1*math.cos(rad1)
    y1=l1*math.sin(rad1)


    x2=x1+(l2*math.cos(rad2))
    y2=y1+(l2*math.sin(rad2))

    #print(t)
    #print(x1,'mm')
    #print(y1,'mm')

    ##BRUSH 
    brush=4000
    brush_point=4000*(30/100)
    brush_left=brush-brush_point
    x3=x2-(brush_point*math.cos(0.3490658503988659))
    y3=y2-(brush_point*math.sin(0.3490658503988659))

    x9=x2+(brush_left*math.cos(0.3490658503988659))
    y9=y2+(brush_left*math.sin(0.3490658503988659))

    y4=y0-1245
    x4=x0

    y5=y4
    x5=x4+4000

    x6=x0+4000
    y6=y0

    x7=4000+(2000*math.cos(0.3490658503988659))
    y7=(2000*math.sin(0.3490658503988659))

    x8=4000-(2000*math.cos(0.3490658503988659))
    y8=-(2000*math.sin(0.3490658503988659))
    plt.plot([x0,x1],[y0,y1])
    plt.plot([x1,x2],[y1,y2])
    plt.plot([x2,x3],[y2,y3])
    plt.plot([x2,x9],(y2,y9))
    plt.xlim(-500,10000)
    plt.ylim(-1500,3000)
    plt.plot([x0,x4],[y0,y4])
    plt.plot([x6,x5],[y6,y5])
    plt.plot([x6,x7],[y6,y7])
    plt.plot([x6,x8],[y6,y8])
    plt.pause(0.01)
    if i<(w-1):
        plt.clf()

#Xcurrent_pos=Xcurrent_pos1


#Zcurrent_pos=Zcurrent_pos1
plt.show()


#theta4=20
#rad4=theta4*math.pi/180
#print(rad4)    

