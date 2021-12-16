import numpy as np

f = open("values.txt", "r")
numbers = f.read().split("\n")
grupN =0
posNumber =0
lst = [1,2,3,4,5,6,7,8]
numbers_grups = np.zeros( (len(numbers), 3) )

for x in range(len(numbers)):
    #if(numbers[x] != numbers[len(numbers)-1]):
    for i in range(3):
        if x+i < len(numbers):
            numbers_grups[x][i]= numbers[x+i]
        else:
            numbers_grups[x][i]=numbers[x]
sumaAnterior=-1
x=-1
suma=0
i =0
for grup in numbers_grups:
    suma=0
    for num in grup:
        suma += num
    if suma > sumaAnterior:
        x+=1
    sumaAnterior = suma
    i+=1
print(x)

