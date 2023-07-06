suma = 6
resta = suma -2
print("m" , resta)

a="hola mundo"
print( a[2])

codigo="HGorlaac?isarsq!"
pal=""
for i in range(len(codigo)):
    if i%2== 1:
        pal = pal + codigo[i]
print(pal)        


codigo="HGorla*c?isarsq!"
pal=""
for i in range(len(codigo)):
    if codigo[i]== "*":
        break
    if i%2== 1:
        pal = pal + codigo[i]
print(pal)    

lista =list()
print(type(list))

dic = {"color": "rojo"}
print(dic["rojo"])
       