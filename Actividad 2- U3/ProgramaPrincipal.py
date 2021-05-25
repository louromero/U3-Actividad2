from Helado import Helado
from Sabor import Sabor
from ManejadorHelado import ManejadorHelado
from ManejadorSabor import ManejadorSabor

def imprimir():
    print("\n-------------HELADERIA----------------")
    print("---------------MENU-------------------")
    print("1. Registrar venta.")
    print("2. Listar sabores mas vendidos.")
    print("3. Mostrar total de gramos vendidos por sabor.")
    print("4. Mostrar los sabores mas vendidos por helado.")
    print("0. SALIR")
    print("--------------------------------------\n")

def gramos():
    print("\n--------------GRAMOS-----------------")
    print("1. 100gr")
    print("2. 150gr")
    print("3. 250gr")
    print("4. 500gr")
    print("5. 1000gr")
    print("--------------------------------------\n")

def menu():
    band=True
    while band:
        imprimir()
        opcion=int(input("Ingrese opcion: "))

        #--------------------------------------------OPCION 1
        if opcion==1:
            bandera=True
            #ELECCION DEL PESO
            eleccionHelado={1: 100,2:150,3:250,4:500,5:1000}
            gramos()
            while bandera:
                op=int(input("Ingrese opcion: "))
                if op==0 or op<=5:
                    bandera=False
                elif op > 5:
                    print("\nOpcion incorrecta, intente de nuevo.")
            sabores=[]
            op1=1
            n=1
            bandera2=True
            #ELECCION DE LOS SABORES
            while bandera2 and n<=4:
                print("\nElegir sabor n° {}\n".format(n))
                for x in manejadorSabor.getSabores():
                    print("{}. {}\n{}\n".format(x.getNumero(),x.getNombre(),x.getDescripcion()))
                print("Ingrese 0 pasa salir.")
                op1=int(input("\nIngrese opcion: "))
                if op1<=len(manejadorSabor.getSabores()) and op1>0:
                    sabores.append(manejadorSabor.getSabor(op1))
                    n+=1
                elif op1==0:
                    bandera2=False
                else:
                    print("\nOpcion incorrecta. Intente de nuevo.")
            #GUARDAR PRODUCTO
            if len(sabores)==0:
                print("\nNo se agregaron sabores. Venta cancelada.")
            elif len(sabores)>0:
                nuevoHelado=Helado(eleccionHelado[op],sabores)
                manejadorHelado.setHelado(nuevoHelado)
                print("\nVenta realizada con exito :)")

        #------------------------------------------OPCION 2
        elif opcion==2:
            mayores=manejadorHelado.getMayor(manejadorHelado,manejadorSabor)
            print("Los sabores más pedidos son:")
            for s in mayores:
                print(s)

        #--------------------------------------------OPCION 3
        elif opcion==3:
            print(" ")
            for x in manejadorSabor.getSabores():
                print("{}. {}\n{}\n".format(x.getNumero(),x.getNombre(),x.getDescripcion()))
            n=int(input("N° de sabor para mostrar total de gramos vendidos: "))
            manejadorHelado.getTotalGramo(n)

        #---------------------------------------------OPCION 4
        elif opcion==4:
            eleccionHelado={1: 100,2:150,3:250,4:500,5:1000}
            gramos()
            op=int(input("Ingrese opcion: "))
            lista=manejadorHelado.getTotalSaboresV(op)
            for k in lista:
                print(k)

        elif opcion==0:
            print(":) Chau.")
            band=False
        else:
            print("\nOpcion no valida.")


if __name__=='__main__':
    manejadorSabor=ManejadorSabor()
    manejadorHelado=ManejadorHelado()
    manejadorSabor.testSabores()
    menu()