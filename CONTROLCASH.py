# Creamos listas y contadores
nombres = []  
gastos = []   
total = 0     
personas = 0  

print("BIENVENIDOS A CONTROLCASH")
print("\nPara terminar escribe exactamente 'FIN' ")

#Pedimos el primer nombre
nombre = input("Nombre de la Persona 1: ")

# Bucle para añadir los nombres y gastos a las listas
while nombre != "FIN":
    nombres.append(nombre) 
    print("Gasto de", nombre, ":")
    gasto = float(input("Introduce la cantidad en euros:"))
    gastos.append(gasto)
    total += gasto
    personas += 1
    print("Gasto acumulado:", total)
    nombre = input("Siguiente nombre (o FIN): ")

#Calculamos el gasto de cada persona 
if personas >= 2:
    media = total / personas
    print("\nRESULTADOS")
    print("Personas:", personas)
    print("Gasto total:", total, "€")
    print("Gasto por persona:", media,"€")
    print(" SALDOS ")

    # Añadimos mensajes divertidos aleatorios
    import random

    mensajes_deuda = ["¡Hora de pagar! 💸", "Saca la billetera 😅", "No te escapes 😉"]
    mensajes_cobro = ["¡Tienes suerte! 😎", "Disfruta tu dinero 🤑", "Eres millonario hoy 🏦"]
    mensajes_nada = ["¡Equilibrio perfecto! ✨", "¡Todos contentos! 😄", "¡Sin deudas por hoy! 🎉"]

    #Bucle para calcular saldos
    posicion = 0
    while posicion < personas:
        nombre1 = nombres[posicion]
        gasto1 = gastos[posicion]
        saldo = gasto1 - media
        saldo1 = round(saldo, 2)

        if saldo < 0:
            print("\033[91m", nombre1, "debe", -saldo1,"€", random.choice(mensajes_deuda), "\033[0m")
        elif saldo > 0:
            print("\033[92m", nombre1, "cobra", saldo1,"€", random.choice(mensajes_cobro), "\033[0m")
        else:
            print("\033[93m", nombre1, "no debe nada", random.choice(mensajes_nada), "\033[0m")

        posicion += 1

else:
    print("ERROR: Se necesitan al menos 2 personas para dividir los gastos.")
