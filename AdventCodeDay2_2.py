import numpy as np
#Open file python
f = open("values.txt", "r")
dades = f.read().split("\n")
x =0
aim=0
depth =0
for i in range(len(dades)):
  if dades[i].find("forward") != -1:
    x+= int(dades[i].split("forward ")[1])
    depth +=aim*int(dades[i].split("forward ")[1])
  elif dades[i].find("up") != -1:
    aim -=int(dades[i].split("up ")[1])
  elif dades[i].find("down") != -1:
    aim +=int(dades[i].split("down ")[1])
print("Position: x: "+str(x)+" Aim: "+str(abs(aim))+" Depth: "+str(depth))
print("Total: "+str(abs(x*depth)))