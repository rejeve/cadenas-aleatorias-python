import random

def generar_cadenas(cantidad,longitud):
    caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
                   "y","x","z","1","2","3","4","5","6","7","8","9","0"]
    
    # Calcular el maximo de combinaciones posibles dada la longitud
    totalCombinaciones = (36) ** longitud

    palabrasAleatorias = set()

    if cantidad > totalCombinaciones:

        while len(palabrasAleatorias) < totalCombinaciones:
                cadena = ""
                for i in range(longitud):
                    cadena += random.choice(caracteres)
                palabrasAleatorias.add(cadena)
        print(palabrasAleatorias)
        print("No se pudieron generar todas las palabras únicas\n" \
        "Se generaron " , len(palabrasAleatorias), "palabras")

    else:
        while len(palabrasAleatorias) < cantidad:
                cadena = ""
                for i in range(longitud):
                    cadena += random.choice(caracteres)
                palabrasAleatorias.add(cadena)
        print(palabrasAleatorias)
        print("Se generaron", len(palabrasAleatorias), "palabras")
    

n = int(input("Longitud de cadena: "))
o = int(input("Cantidad de palabras: "))

generar_cadenas(o,n)