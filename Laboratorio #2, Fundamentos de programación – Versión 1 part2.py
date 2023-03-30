print("*********************************")
print("Bienvenid@ al programa de números")
print("*********************************")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El número", num1 , "es el número más grande de los tres")
elif num1 < num2 and num1 < num3:
    print("El numero", num1, "es el numero mas pequeño de los tres")
else:
    print("El numero", num1, "es el numero mediano de los tres")


if num2 > num1 and num2 > num3:
    print("El número", num2 , "es el número más grande de los tres")
elif num2 < num1 and num2 < num3:
    print("El numero", num2, "es el numero mas pequeño de los tres")
else:
    print("El numero", num2, "es el numero mediano de los tres")

if num3 > num1 and num3 > num2:
    print("El número", num3 , "es el número más grande de los tres")
elif num3 < num2 and num3 < num1:
    print("El numero", num3, "es el numero mas pequeño de los tres")
else:
    print("El numero", num3, "es el numero mediano de los tres")

print("FIN")