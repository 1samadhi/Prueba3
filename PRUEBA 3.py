# Lista para almacenar las reservas
reservas = []

# Registrar Reserva Para registrar una reserva se requiere lo siguiente: Nombre y apellido del cliente, 
# ciudad de origen, detalle del tour. Por ejemplo, la empresa ofrece tours a Torres del Paine, Carretera Austral y Chiloé. Debe permitir seleccionar
# entre 1 de las 3 opciones e ingresar la cantidad de personas para el tour

def registrar_reserva(nombre, apellido, ciudad_origen, destino, cantidad_personas):   
    reserva = { # Se crea una lista
        "Nombre": nombre,
        "Apellido": apellido,
        "Ciudad de origen": ciudad_origen,
        "Destino": destino,
        "Cantidad de personas": cantidad_personas
    }

    reservas.append(reserva)  # Agrega la reserva a la lista de reservas
    print("Registro ingresado con éxito")

# Solicitar datos del usuario y registrar una nueva reserva
def solicitar_datos_reserva():
    nombre = input("Ingrese su nombre: ").strip().title()  # Solicita el nombre .stip() eliminaremos espacios innecesarios y .title() nos aseguramos que sólo la primera letra sea mayúscula
    apellido = input("Ingrese su apellido: ").strip().title()  # Solicita el apellido
    ciudad_origen = input("Ingrese su ciudad de origen: ").strip().title()  # Solicita la ciudad de origen

    # Solicita el destino y valida la opción ingresada
    print("----Seleccione su destino marcando el número correspondiente----")
    print("1. Torres del Paine")
    print("2. Carretera Austral")
    print("3. Chiloe")
    destino_opcion = input("Seleccione un número como destino: ")

    if destino_opcion == '1':
        destino = 'Torres del Paine'
    elif destino_opcion == '2':
        destino = 'Carretera Austral'
    elif destino_opcion == '3':
        destino = 'Chiloe'
    else:
        print("Opción de destino no válida.")  # Agrega una validación para opciones incorrectas
        return  # Sale de la función si el destino no es válido
    
    cantidad_personas = input("Ingrese la cantidad de pasajeros: ")
    if not cantidad_personas.isdigit(): #con .isdigit() me aseguro que sólo ingresen números
        print("La cantidad de personas debe ser un número entero.")  # Valida que la cantidad de personas sea un número
        return  # Sale de la función si la cantidad no es válida
    
    # Llama a la función para registrar la reserva con los datos ingresados
    registrar_reserva(nombre, apellido, ciudad_origen, destino, int(cantidad_personas))  # Llama a la función con los argumentos

""" Listar Reservas Debe mostrar en la pantalla la lista de todas las reservas realizadas similar al ejemplo anterior de registro de
reservas"""

def listar_reserva():
    if not reservas:  # Verifica si la lista de reservas está vacía
        print("No hay reservas registradas.")
    else:
        # Imprimir los encabezados
        print(f"{'Nombre':<20} {'Apellido':<20} {'Ciudad de Origen':<20} {'Destino':<20} {'Cantidad de Personas':<20}")
        print("="*100)

        for reserva in reservas:
            # Imprime cada reserva en el formato adecuado
            print(f"{reserva['Nombre']:<20} {reserva['Apellido']:<20} {reserva['Ciudad de origen']:<20} {reserva['Destino']:<20} {reserva['Cantidad de personas']:<20}")

""" Imprimir Detalle de Reservas por Destino Para imprimir el detalle de reservas, el usuario debe seleccionar alguno de los destinos
donde es posible realizar un tour. Estos destinos deben estar previamente definidos en algún tipo de colección de Python en el
código y por lo menos deben ser tres. Por ejemplo: Torres del Paine, Carretera Austral, Chiloé. Al seleccionar uno de los destinos,
se generará un archivo de texto (.txt) con el detalle de las reservas que se deberá llevar a ese destino."""

def imprimir_detalle_por_destino(destino):
    # Genera un nombre de archivo basado en el destino y convierte a minúsculas
    archivo_nombre = f"reservas_{destino.lower()}.txt"
    with open(archivo_nombre, 'w') as archivo:
        archivo.write(f"--- Detalle de Reservas para {destino} ---\n\n")
        archivo.write(f"{'Nombre':<20} {'Apellido':<20} {'Ciudad de Origen':<20} {'Destino':<20} {'Cantidad de Personas':<20}\n")
        for reserva in reservas:
            if reserva['Destino'] == destino:
                # Escribe cada reserva en el archivo de texto
                archivo.write(f"{reserva['Nombre']:<20} {reserva['Apellido']:<20} {reserva['Ciudad de origen']:<20} {reserva['Destino']:<20} {reserva['Cantidad de personas']:<20}\n")
    print(f"Detalle de reservas para {destino} guardado en {archivo_nombre}.")

# Salir del Programa El programa debe funcionar hasta que el usuario decida salir.

def menu():
    while True:
        print("-----MENÚ PRINCIPAL-----\n\n")
        print("1. Registrar reserva")
        print("2. Lista de reservas")
        print("3. Descargar destinos registrados")
        print("4. Salir")
        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            solicitar_datos_reserva()  # Llama a la función para solicitar datos de la reserva

        elif opcion == '2':
            listar_reserva()  # Llama a la función para listar las reservas

        elif opcion == '3':
            destino = input("Ingrese el destino para el informe: ").strip().title()  # Solicita el destino para el informe
            # Llama a la función para imprimir el detalle por destino
            imprimir_detalle_por_destino(destino)  

        elif opcion == '4':
            break  # Sale del bucle y termina el programa

        else: 
            print("Escoge una opción válida")  # Mensaje de error para opciones no válidas

menu()  # Llama a la función del menú para iniciar el programa