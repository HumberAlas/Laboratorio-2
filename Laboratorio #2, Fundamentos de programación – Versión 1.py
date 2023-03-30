#datos de el costo de un articulo vendido y la cantidad de dinero entregado por el cliente
#El cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del producto.
#¿Qué pasa si el cliente paga exactamente lo que vale el producto?
#La cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto.

menu = input('''
            Menú de articulos de herramientas
            1- Llave inglesa
            2- Cepillo metalico
            3- Limas
            4- Destornillador
            5- Taladro
            Ingresa el articulo que quieres comprar -> ''')

Llaveinglesa = 25
Cepillometalico =10
Limas = 6
Destornillador = 8
Taladro = 45

if menu == "Llave inglesa" or menu == "1":
    print("El precio de este producto es de $25")
    dinero = int(input("Ingrese la cantidad de dinero: "))
    if dinero == 25:
        print("Ha entregado lo exacto, muchas gracias por su compra")
    elif dinero > 25:
        cambio = dinero - Llaveinglesa
        print("Usted ha entregado demas, asi qué se le dará un cambio de:" , cambio , "dolar/es")
    elif dinero < 25:
        falta = Llaveinglesa - dinero
        print("Lo sentimos, pero aún no hay dinero suficiente para pagar, aún debe un total de: ", falta , "dolar/es")
elif menu == "Cepillo metalico" or menu == "2":
    print("El precio de este producto es de $10")
    dinero = int(input("Ingrese la cantidad de dinero: "))
    if dinero == 10:
        print("Ha entregado lo exacto, muchas gracias por su compra")
    elif dinero > 10:
        cambio = dinero - Cepillometalico
        print("Usted ha entregado demas, asi qué se le dará un cambio de:" , cambio , "dolar/es")
    elif dinero < 10:
        falta = Cepillometalico - dinero
        print("Lo sentimos, pero aún no hay dinero suficiente para pagar, aún debe un total de: ", falta , "dolar/es")
elif menu == "Limas" or menu == "3":
    print("El precio de este producto es de $6")
    dinero = int(input("Ingrese la cantidad de dinero: "))
    if dinero == 6:
        print("Ha entregado lo exacto, muchas gracias por su compra")
    elif dinero > 6:
        cambio = dinero - Limas
        print("Usted ha entregado demas, asi qué se le dará un cambio de:" , cambio , "dolar/es")
    elif dinero < 6:
        falta = Limas - dinero
        print("Lo sentimos, pero aún no hay dinero suficiente para pagar, aún debe un total de: ", falta , "dolar/es")
elif menu == "Destornillador" or menu == "4":
    print("El precio de este producto es de $8")
    dinero = int(input("Ingrese la cantidad de dinero: "))
    if dinero == 8:
        print("Ha entregado lo exacto, muchas gracias por su compra")
    elif dinero > 8:
        cambio = dinero - Destornillador
        print("Usted ha entregado demas, asi qué se le dará un cambio de:" , cambio , "dolar/es")
    elif dinero < 8:
        falta = Destornillador - dinero
        print("Lo sentimos, pero aún no hay dinero suficiente para pagar, aún debe un total de: ", falta , "dolar/es")
elif menu == "Taladro" or menu == "5":
    print("El precio de este producto es de $45")
    dinero = int(input("Ingrese la cantidad de dinero: "))
    if dinero == 45:
        print("Ha entregado lo exacto, muchas gracias por su compra")
    elif dinero > 45:
        cambio = dinero - Taladro
        print("Usted ha entregado demas, asi qué se le dará un cambio de:" , cambio , "dolar/es")
    elif dinero < 45:
        falta = Taladro - dinero
        print("Lo sentimos, pero aún no hay dinero suficiente para pagar, aún debe un total de: ", falta , "dolar/es")
else: 
    print("El dato que ingresaste no se encutra\n")
print("FIN")