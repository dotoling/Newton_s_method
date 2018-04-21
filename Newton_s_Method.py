import numpy as np
import math
from sympy import *

x = symbols('x')
y = symbols('y')
#f_x 을 추가 하기 위해서는 이곳을 참고하십시오
f_x = []
f_x.append(np.e**x - 3)
f_x.append(x-3)
f_x.append(x**2-4*x+4)

X_Data = []
X_0 = int(input('X_0 값을 입력해주십시오 : '))
X_Data.append(X_0)

def Newton_method(f_x):
    for i in range(0,100):
        X_Data.append(np.float64(X_Data[i]) - ((f_x.subs(x,np.float64(X_Data[i])))/(diff(f_x).subs(x,np.float64(X_Data[i])))))
    return X_Data

def NUM_SET(xmin,xmax,ymin,ymax):
    NUM =[]
    NUM.append(xmin)
    NUM.append(xmax)
    NUM.append(ymin)
    NUM.append(ymax)
    return NUM

def draw_plot(f_x,num):
    if(num==0):
        NUM = NUM_SET(-1,8,-5,200)
    elif(num==1):
        NUM = NUM_SET(-10,10,-10,10)
    elif(num==2):
        NUM = NUM_SET(-20,20,-20,20)
    else:
        print('없는 값이 들어왔습니다 확인 해주십시오...')
    y_1 = f_x
    X = Newton_method(f_x)
    #print(X)
    for j in range(0,5):
        HEAD = (diff(f_x).subs(x,(X[j])))
        TAIL_1 = -((diff(f_x).subs(x,(X[j])))*(X[j]))
        TAIL_2 = (f_x.subs(x,X[j]))
        TAIL = TAIL_1 + TAIL_2
        y_2 = HEAD*x + TAIL
        VerticalLine = X[j]
        DOT = solve(Eq((x-X[j+1])**2+y**2,0.01 ),y)
        p=plot(y_1,y_2,DOT[0],DOT[1],xlim=[NUM[0],NUM[1]], ylim=[NUM[2],NUM[3]],show=False)
        p[1].line_color = "green"
        p[2].line_color = 'red'
        p[3].line_color = 'red'
        p.show()
print('\n함수 번호')

for i in range(0,len(f_x)):
    print('번호',i,':', f_x[i])

DEF_F_X = int(input('\n번호를 입력해주십시오 : '))

for k in range(0,len(f_x)):
    if (DEF_F_X==k):
        draw_plot(f_x[k],k)
    else:
        pass




