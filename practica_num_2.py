''' Desarrolle una clase que cumpla con las siguientes funciones para crear, modificar, eliminar, listar el modelo.
(Para el proceso de guardado puede usar archivos locales con Pickle o JSON) Generar UI vía interfaz de comandos (CLI)
para usar las diferentes funciones. El modelo para la clase es un usuario con datos simples como: ·Nombres ·Apellidos
·Edad ·Email '''

'''Commands: 
create-user --> ingresar datos del usuario al archivo 
delete-users  -->   eleimina los datos del archivo
open-users -->  abre el archivo y muestra los datos
update-user --> actualiza el datos del archivo '''

import pickle
import click
import os


def menu():
    os.system('clear')
    print("Selecciona una opción")
    print("\t1 - Modificar nombre")
    print("\t2 - Modificar apellido")
    print("\t3 - Modificar edad")
    print("\t4 - Modificar E-mail")
    print("\t5 - salir")

def open_doc():
    with open('archivo.pkl', 'r+b') as arch:
        open_user = pickle.load(arch)
        print("Los datos actuales en el archivo son: ", open_user.__dict__)

def save_doc(open_user):
    with open('archivo.pkl', 'wb') as archive:
        pickle.dump(open_user, archive)

class User():
    def __init__(self, name, lastname, age, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email

    def __str__(self):
        return self.name + ' ' + self.lastname + ' ' + self.age + ' ' + str(self.email)


@click.group()
def main():
    pass

@main.command()
@click.option('--name', prompt='Ingresa el nombre del usuario')
@click.option('--lastname', prompt='Ingresa el apellido del usuario')
@click.option('--age', prompt='Ingresa la eda del usuario')
@click.option('--email', prompt='Ingresa el E-mail del usuario')
def create_user(name, lastname, age, email):
    user = User(name, lastname, age, email)
    print("Los datos almacenados en el archivo son:"
          " \n Nombre:", user.name, "\n Apellido:", user.lastname, "\n Edad:", user.age, "\n E-mail:", user.email)
    save_doc(user)

@main.command()
def open_users():
    if os.stat('archivo.pkl').st_size == 0:
        print("El archivo esta vacio")
    else:
        open_doc()

@main.command()
def update_user():
    with open('archivo.pkl', 'r+b') as arch:
        open_user = pickle.load(arch)
        print(open_user.__dict__)
    while True:
        menu()
        opcionMenu = input("inserta un numero valor >> ")
        if opcionMenu == "1":
            input("Has pulsado la opcion modificar nombre: \npulsa una tecla para continuar")
            open_doc()
            name = input("ingresa el nuevo nombre: ")
            open_user.name = name
            print(open_user.__dict__)
            save_doc(open_user)
        elif opcionMenu == "2":
            input("Has pulsado la opcion modificar apellido: \npulsa una tecla para continuar")
            open_doc()
            last_name = input("ingresa el nuevo apellido: ")
            open_user.lastname = last_name
            print(open_user.__dict__)
            save_doc(open_user)
        elif opcionMenu == "3":
            input("Has pulsado la opcion modificar edad: \npulsa una tecla para continuar")
            open_doc()
            age = input("ingresa la nueva edad: ")
            open_user.age = age
            print(open_user.__dict__)
            save_doc(open_user)
        elif opcionMenu == "4":
            input("Has pulsado la opcion modificar e-mail: \npulsa una tecla para continuar")
            open_doc()
            mail = input("ingresa el nuevo e-mail: ")
            open_user.email = mail
            print(open_user.__dict__)
            save_doc(open_user)
        elif opcionMenu == "5":
            break
        else:
            input("Error opcion incorrecta \n pulsa una tecla para continuar")

@main.command()
def delete_users():
    aux = input("¿Desea borrar el contenido del archivo? S/N ")
    if aux == 's':
        with open("archivo.pkl", 'r+') as archive:
            archive.truncate(0)
        print("Los datos del archivo fueron borrados con exito")
    else:
        print("Se aborta el borrado de datos")

if __name__ == '__main__':
    main()

