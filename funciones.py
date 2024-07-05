import list
import random
codig = random in range(100000,999999)

def menu_principal():
    while True:
        print("---Menu Principal---")
        print("1. Registrar consumo: ")
        print("2. listar todos los consumos: ")
        print("3. Imprimir hoja consumo")
        print("4. buscar consumo por ID")
        print("5. Salir")
        
        opc = int(input("eligue una opcion del menu: "))
        if  opc == 1:
            registrar()
        elif opc == 2:
            listar()
        elif opc == 3:
            print("k")
        elif opc == 4:
            print("bros")
        elif opc == 5:
            print("saliendo...")
            break
        else:
                print("solo se aceptan numeros 1/5")
    return True


def registrar():
    while True:
      print("tu ID es: ",codig)
      nombre = input("ingrese el nombre del jugador: ").strip
      nombre = nombre
      edad = int(input("ingrese la edad del jugador: "))
      if edad != 0:
         print("ingrese el equipo del jugador: ")
         print("1. Lol")
         print("2. Valo")
         print("3. Osu")
         equipo = int(input(""))
         if equipo == "1":
             list.contador_equipos.append[0]
         elif equipo == 2:
             list.contador_equipos.append[1]
         elif equipo == 3:
             list.contador_equipos.append[2]
         cafe = input("ingrese cuanto cafe toma el jugador: ")
         if cafe == cafe:
               print("")
               break
         elif cafe == "":
               print("no puede quedar vacio")
               return True
      else:
            print("edad invalida vuelva a intentarlo ")
            break


def listar(equipos):
    print(f"{equipos}")

def imprimir_hoja():
    print(f"nombre: ")
    print(f"edad: ")
    print(f"equipo: ")
    print(f"cantidad de cafe: ")