# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 13:55:50 2017

@author: willi
"""

def mergeSort(alist1,alist2):
    if len(alist1)>1:
        mid = len(alist1)//2
        lefthalf = alist1[:mid]
        righthalf = alist1[mid:]
        l2 = alist2[:mid]
        r2 = alist2[mid:]
        mergeSort(lefthalf,l2)
        mergeSort(righthalf,r2)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist1[k]=lefthalf[i]
                alist2[k]=l2[i]
                i=i+1
            else:
                alist1[k]=righthalf[j]
                alist2[k]=r2[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist1[k]=lefthalf[i]
            alist2[k]=l2[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist1[k]=righthalf[j]
            alist2[k]=r2[j]
            j=j+1
            k=k+1
    #print("Merging ",alist1)
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

archivo = open("pato2.txt","r")

lines = archivo.readlines()
iniy = len(lines)
inix = 0


xd1=[]
yd1=[]
xd2=[]
yd2=[]


print(iniy," ",inix)
for line in lines:
    inix = 0
    for c in line:
        if( c == '1' ):
            xd1.append(inix)
            yd1.append(iniy)
        elif( c == '2' ):
            xd2.append(inix)
            yd2.append(iniy)
        inix+=1
    iniy-=1

archivo.close();
mergeSort(xd1,yd1);
mergeSort(xd2,yd2);


print(xd1)
print(yd1)


xd1i = np.linspace(min(xd1), max(xd1), num=1001)  # Dominio
yd11d = np.interp(xd1i, xd1, yd1)
#yd11d = InterpolatedUnivariateSpline(xd1i, yd1i, k=1)(xd1)  # Mismo resultado
yd1sp = InterpolatedUnivariateSpline(xd1, yd1)(xd1i)  # Llamamos a la clase con xu

xd2i = np.linspace(min(xd2), max(xd2), num=1002)  # Dominio
yd22d = np.interp(xd2i, xd2, yd2)
#yd22d = InterpolatedUnivariateSpline(xd2i, yd2i, k=2)(xd2)  # Mismo resultado
yd2sp = InterpolatedUnivariateSpline(xd2, yd2)(xd2i)  # Llamamos a la clase con xu



print(yd1sp)
print (yd2sp)

plt.figure(1)
plt.title("Interpolada")
plt.plot(xd1i,yd1sp)
plt.plot(xd2i,yd2sp)



plt.figure(2)
plt.title("Real")
plt.plot(xd1,yd1)
plt.plot(xd2,yd2)

plt.show()