import numpy as np
#Open file python
f = open("values1.txt", "r")
dades = f.read().split("\n")
def count_bits_mes_pes(dades, pes):
  one=0
  zero=0
  for num in dades:
    if int(num[pes]) == 1:
      one+=1
    else:
      zero +=1
  if one > zero:
    return 1
  else:
    return 0
def count_bits_menys_pes(dades, pes):
  one=0
  zero=0
  for num in dades:
    if int(num[pes]) == 1:
      one+=1
    else:
      zero +=1
  print(str(one)+" "+str(zero))
  if one < zero:
    return 1
  else:
    return 0
gamma=""
epsilon=""
for x in range(len(dades[0])):
  gamma+=str(count_bits_mes_pes(dades,x))
  epsilon+=str(count_bits_menys_pes(dades,x))
gamma = int(gamma,2)
epsilon = int(epsilon,2)
print("Totat: "+str(gamma*epsilon))