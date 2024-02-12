cantidad_u = int(input("numero de elementos del conjunto u "))
cantidad_a = int(input("numero de elementos del conjunto a "))
u=set()
for i in range(cantidad_u):
  elemento = float(input("elemento"+ str(i+1)+": "))
  u.add(elemento)
print(u)

a=set()
for i in range(cantidad_a):
  elemento = float(input("elemento"+ str(i+1)+": "))
  a.add(elemento)
print(a)

print("1) (u|a)&a \n 2) (u&a)^a \n 3) (u-a)^a")
op=int(input())
if op==1:
  R=(u|a)&a
  print(R)
if op==2:
  R=(u&a)^a
  print(R)
if op==3:
  R=(u-a)^a
  print(R)


