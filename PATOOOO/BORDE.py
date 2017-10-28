archivo = open("pato.txt","r")

lines = archivo.readlines()
iniy = len(lines)
cols=0
filas=0

matriz = []
temp=[]

print("--",archivo)

for line in lines:
   # print (line)
    matriz.append([])
    cols=0;
    for c in line:
        #print(c,"--->")
        matriz[filas].append(c)
        cols=cols+1
    matriz[filas].append('\n')    
    filas=filas+1

print cols
print filas

'''
for x in range(0, filas):
    for y in range(0, cols):
       # print("-->",cols)
        #print("-->>",matriz[x][y])
        if  matriz[x][y] == "\n":
             print(x,"**",y)
             break
        
        if  matriz[x][y] != "-":
           # print(x,"--",y)
            matriz[x][y-1]="1"
            break

print cols
for x in range(0, filas):
    for y in range(2, cols):
       # print("-->",cols)
      #  print("-->>",matriz[x][y])
        if  matriz[x][y] == "\n":
        #    print(x,"**",y)
             break
        if  matriz[x][cols-y] != "-":
           # print(x,"--",y)
            matriz[x][cols-y]="2"
            break
'''

for y in range(0, cols):
    for x in range(0, filas):
       # print("-->",cols)
      #  print("-->>",matriz[x][y])
        if  matriz[x][y] == "1" or matriz[x][y] == "2" or matriz[x][y] == "\n":
        #    print(x,"**",y)
             break

        if  matriz[x][y] != "-":
            #print(x,"--",y)
            matriz[x][y]="1"
            break

for y in range(0, cols):
    for x in range(2, filas):
       # print("-->",cols)
      #  print("-->>",matriz[x][y])
        if  matriz[x][y] == "\n":
            #print(x,"**",y)
            break

        if  matriz[filas-x][y] != "-":
            #print(x,"--",y)
            matriz[filas-x][y]="2"
            break
        
        

for y in range(0, filas):
    for x in range(0, cols):
       # print("-->",cols)
      #  print("-->>",matriz[x][y])
        if  matriz[y][x] == "1":
            tem=x+1;
            tem2=tem+1;
            while matriz[y][tem2] == "1":
                matriz[y][tem]="+"
                tem+=1
                tem2+=1
        if  matriz[y][x] == "2":
            tem=x+1;
            tem2=tem+1;
            while matriz[y][tem2] == "2":
                matriz[y][tem]="+"
                tem+=1
                tem2+=1



'''for x in range(0, filas):
     for y in range(0, cols):
          print matriz[x][y],#
     print("\n")'''

print("--")
file=open("pato2.txt","w")
#file.write('\n')
for x in range(0, filas):
     for y in range(0, cols):
         #print matriz[x][y]
         file.write(matriz[x][y])
     '''if  matriz[x][cols-1] != "\n":
         file.write('\n')'''
file.close();


archivo.close();
