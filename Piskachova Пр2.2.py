x = "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80"
y = "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb"

Sum = hex(int(x, 16) + int(y, 16))
Subtraction=hex(int(x, 16) - int(y, 16))
Product=hex(int(x, 16) * int(y, 16))
Modulo =hex(int(x, 16) % int(y, 16))
print("Sum=",Sum)
print("Subtraction=",Subtraction)
print("Product=",Product)
print("Modulo=",Modulo)

a = int(y, 16)  
b = int(x, 16)   
c= a // b
Division=hex(c)
print("Division=",Division)  
d=~a
Inversion= hex(d)  
print("Inversion=",Inversion) 




    




