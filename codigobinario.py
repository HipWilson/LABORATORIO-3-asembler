def binario_a_decimal(binario):
    return int(binario, 2)

def decimal_a_binario(decimal):
    return bin(decimal)[2:].zfill(8)

print("Elige una opción:")
print("1. Convertir de binario a decimal")
print("2. Convertir de decimal a binario")

opcion = input("> ")

if opcion == "1":
    binario = input("Ingresa un número binario de 8 dígitos: ")
    if len(binario) == 8 and all(c in "01" for c in binario):
        print("Decimal:", binario_a_decimal(binario))
    else:
        print("Error: Ingresa un número binario válido de 8 dígitos.")

elif opcion == "2":
    try:
        decimal = int(input("Ingresa un número decimal entre 0 y 255: "))
        if 0 <= decimal <= 255:
            print("Binario:", decimal_a_binario(decimal))
        else:
            print("Error: El número debe estar entre 0 y 255.")
    except ValueError:
        print("Error: Ingresa un número válido.")

else:
    print("Opción no válida.")
