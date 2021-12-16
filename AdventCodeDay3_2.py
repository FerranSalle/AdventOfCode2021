import numpy as np
#Open file python
f = open("values.txt", "r")
data = f.read().split("\n")
data1 = data.copy()
number_len = len(data[0])
oxygen =0
CO2=0
#Function to keep only the numbers that contains 1 in one specific position
def count_bits_mes_pes(dades, pes):
  one=0
  zero=0
  try:
    for num in dades:
      if int(num[pes]) == 1:
        one+=1
      else:
        zero +=1
    if one >= zero:
      for y in range(len(dades)):
        if int(dades[y][pes]) != 1:
          data[y] = 0
    else:
      for y in range(len(dades)):
        if int(dades[y][pes]) != 0:
          data[y] = 0
  except:
    print(dades)
#Function to keep only the numbers that contains 0 in one specific position
def count_bits_menys_pes(dades, pes):
  one=0
  zero=0
  try:
    for num in dades:
      if int(num[pes]) == 1:
        one+=1
      else:
        zero +=1
    if one < zero:
      for y in range(len(dades)):
        if int(dades[y][pes]) == 0:
          data1[y] = 0
    elif one == zero:
      for y in range(len(dades)):
        if int(dades[y][pes]) == 1:
          data1[y] = 0
    else:
      for y in range(len(dades)):
        if int(dades[y][pes]) == 1:
          data1[y] = 0
  except:
    print(dades)
  try:
    dades = list(set(dades))
    dades.remove(0)
  except:
    pass
  



for x in range(number_len):
  if len(data)>=2: 
    count_bits_mes_pes(data,x)
    data = list(set(data))
    try:
      data.remove(0)
    except:
      pass
  if len(data1) >=2:
    count_bits_menys_pes(data1,x)
    data1 = list(set(data1))
    try:
      data1.remove(0)
    except:
      pass
oxygen = int(data[0],2)
CO2 = int(data1[0],2)
print("Total: "+str(oxygen*CO2))