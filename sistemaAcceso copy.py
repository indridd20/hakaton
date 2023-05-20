contraseñas = {}

def menu():
    print("Bienvenido al sistema de control de acceso")
    print("1 - Iniciar sesión")
    print("2 - Registrarse")
    print("3 - Salir")
    option = input("Ingrese una opción: ")
    if option == "1":
        acceder()
    elif option == "2":
        registrar()
    elif option == "3":
        exit()
    else:
        print("Opción inválida")
        menu()

def acceder():
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if nombreUsuario in contraseñas and contraseñas[nombreUsuario] == password:
        print("Inicio de sesión exitoso")
    else:
        print("Nombre de usuario o contraseña incorrectos")
    menu()

def registrar():
    nombreUsuario = input("Ingrese un nombre de usuario: ")
    while nombreUsuario in contraseñas:
        print("El nombre de usuario ya existe, por favor ingrese otro")
        nombreUsuario = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    confirm_password = input("Confirme su contraseña: ")
    while password != confirm_password:
        print("Las contraseñas no coinciden")
        password = input("Ingrese una contraseña: ")
        confirm_password = input("Confirme su contraseña: ")
    contraseñas[nombreUsuario] = password
    print("Registro exitoso")
    menu()

menu()
print("fin del programa")