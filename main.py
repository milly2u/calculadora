from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar varias cifras")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Resultado:", sumar(a, b))

        elif opcion == '2':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Resultado:", restar(a, b))

        elif opcion == '3':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == '4':
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Resultado:", dividir(a, b))

        elif opcion == '5':
            numeros = list(map(float, input("Introduce los números separados por espacio: ").split()))
            print("Resultado:", suma_avanzada(*numeros))

        elif opcion == '6':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige de nuevo.")

if __name__ == "__main__":
    main()