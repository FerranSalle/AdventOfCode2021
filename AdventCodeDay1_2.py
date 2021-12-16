import numpy as np
#Open file python
f = open("values.txt", "r")
grupN =0
numbers = f.read().split("\n")

posNumber =0
numbers_grups = np.zeros( (len(numbers), 3) )

for x in range(len(numbers)):
    for i in range(3):
        if x+i < len(numbers):
            numbers_grups[x][i]= numbers[x+i]
        else:
            numbers_grups[x][i]=numbers[x]
sumaAnterior=0
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
print("Sums that are larger than the previous: "+ str(x))