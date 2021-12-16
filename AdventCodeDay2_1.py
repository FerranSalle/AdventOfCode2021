import numpy as np
#Open file python
f = open("values.txt", "r")
dades = f.read().split("\n")
x =0
y=0

for i in range(len(dades)):
  if dades[i].find("forward") != -1:
    x+= int(dades[i].split("forward ")[1])
  elif dades[i].find("up") != -1:
    y+=int(dades[i].split("up ")[1])
  elif dades[i].find("down") != -1:
    y-=int(dades[i].split("down ")[1])
print("Position: x: "+str(x)+" Position y: "+str(abs(y)))
print("Total: "+str(abs(x*y)))