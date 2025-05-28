from colorama import init, Fore

# Inicializa colorama
init(autoreset=True)

# Función para mostrar el menú
def mostrar_menu():
    print(Fore.CYAN + "\n=== Calculadora Básica ===")
    print("[ 1 ] - Sumar")
    print("[ 2 ] - Restar")
    print("[ 3 ] - Multiplicar")
    print("[ 4 ] - Dividir")
    print("[ 5 ] - Salir")

# Función para pedir números al usuario
def pedir_numero(mensaje):
    while True:
        entrada = input(Fore.YELLOW + mensaje)
        try:
            return float(entrada)
        except ValueError:
            print(Fore.RED + "Error: por favor ingresa un número válido.")

# Función para mostrar los números como enteros si es posible
def formatear_numero(n):
    return int(n) if n == int(n) else n

# Funcion para mostrar la respuesta de la operacion matemática
def mostrar_resultado(num1,num2,operacion,resultado):
    return print(Fore.BLUE + f"Resultado: {num1} {operacion} {num2} = {resultado}")

# Función principal
def calculadora():
    while True:
        mostrar_menu()
        opcion = input(Fore.GREEN + "Selecciona una opción (1-5): ")

        if opcion == '5':
            print(Fore.MAGENTA + "\n¡Gracias por usar la calculadora!")
            break

        if opcion not in ('1', '2', '3', '4'):
            print(Fore.RED + "Opción inválida. Intenta de nuevo.")
            continue

        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        # Guardamos los números formateados
        n1 = formatear_numero(num1)
        n2 = formatear_numero(num2)

        if opcion == '1':
            resultado = formatear_numero(num1 + num2)
            mostrar_resultado(n1,n2,'+',resultado)
        elif opcion == '2':
            resultado = formatear_numero(num1 - num2)
            mostrar_resultado(n1,n2,'-',resultado)
        elif opcion == '3':
            resultado = formatear_numero(num1 * num2)
            mostrar_resultado(n1,n2,'*',resultado)
        elif opcion == '4':
            if num2 == 0:
                print(Fore.RED + "Error: no se puede dividir por cero.")
                continue
            resultado = formatear_numero(num1 / num2)
            mostrar_resultado(n1,n2,'/',resultado)

        while True:
            continuar = input(Fore.CYAN + "\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print(Fore.MAGENTA + "¡Hasta luego!")
                return  # Sale de la función `calculadora`
            else:
                print(Fore.RED + "Opción inválida. Por favor ingresa 's' para sí o 'n' para no.")

# Llamada a la funcion principal
calculadora()
