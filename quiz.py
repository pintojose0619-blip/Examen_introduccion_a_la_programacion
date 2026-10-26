Saldoglobal = 1000

def Deposito(num1):
    if num1 < 0:
        print("La cantidad de dinero debe ser mayor a 0 ")
        return Saldoglobal
    
    else:
        resultado = num1 + Saldoglobal
        return resultado

def retiro(num1):
    if  num1 > Saldoglobal:
        print("Lo sentimos pero el valor a retirar supera su saldo, por favor dijite un valor valido.")
        print("Su saldo actual es: ", Saldoglobal)
        return Saldoglobal
    elif num1 < 0:
        print("Lo sentimos pero para retirar el monto debe ser positivo no negativo. por favor intente nuevamente.")
        print("Su saldo actual es: ", Saldoglobal)
    else:
        resultado = Saldoglobal - num1
        return resultado


def menu():
    print(
"""
*** MENU ***
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
0. Salir.
""")

def leerOpcion():
    
    while True:
        opcion = input("Escriba la opcion que desea. ")
        if opcion < "0" or opcion > "3":       
            print("Error. La opcion ingresada no es válida. ")
            input("Presione ENTER para continuar ... ")
            print("\n\n\n")
            menu()
            pass
        else:
            break
    return int(opcion)

def ConsultarSaldo():
    print("\n\n 1. Consultar el saldo")

    print("Su saldo es de: ", Saldoglobal)

def Depositar():
        print("\n\n 2. Depositar dinero")
        
        while True:
            monto_deposito = int(input("\nIngrese el monto a depositar "))
            if monto_deposito > 0:
           
                print("\nHa realizado exitosamente el deposito por un valor de ",monto_deposito)
                print("\nSu saldo es: ", Deposito(monto_deposito))
                return Deposito(monto_deposito)

            
            else :
                Deposito(monto_deposito)
                

def Retirar():
    print("\n\n 3. Retirar Dinero")
    while True:
        cantidad_retirar = int(input("\nIngrese el monto a retirar "))
        if cantidad_retirar > 0 :
            print("\nHa retirado exitosamente ",cantidad_retirar)
            print("\nSu nuevo saldo es: ", retiro(cantidad_retirar))
            return retiro(cantidad_retirar)
        else:
            retiro(cantidad_retirar)
            
    

while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            ConsultarSaldo()
        case 2:
            Saldoglobal = Depositar()
        case 3:
            Saldoglobal = Retirar()
        case 0:
            print("Gracias por usar nuestro Cajero Automatico...")
            break

    input("Presione ENTER para continuar...")