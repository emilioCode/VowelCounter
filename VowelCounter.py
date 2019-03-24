import msvcrt

#Contador de vocales
#Dando un texto, mostrar cuántas vocales contiene. Si no tiene vocales, no debería imprimirlas. 
#Ejemplo:
#-Entrada: “Hello world!”, Salida: e ->1, o ->2
#-Entrada: “Te amo madre mía”: a -> 3 , e -> 2, i -> 1, o -> 1

print('=========Contador de vocales=========')

string = input("digite un texto: ")

a,e,i,o,u =0,0,0,0,0
if len(string) >0:
    for char in string:#range(len(string)):
        l = char.lower()
        if l =="a": a = a+1
        if l =="e": e = e+1
        if l =="i": i = i+1
        if l =="o": o = o+1
        if l =="u": u = u+1    
else:
    print('vacio')

#print("a-> "+str(a),"e-> "+str(e),"i-> "+str(i),"o-> "+str(o),"u-> "+str(u))
    
if a>0: print("a-> "+str(a))
if e>0: print("e-> "+str(e))
if i>0: print("i-> "+str(i))
if o>0: print("o-> "+str(o))
if u>0: print("u-> "+str(u))

msvcrt.getch()