numero = int(input("Ingrese un número entero: "))  # aqui agregamos el tipo de dato antes de "input"que en este caso en un tipo de dato entero poe lo tanto escribimos "int"

if numero % 2 == 0:  # aqui agregamos doble signo de "=" ya que solo habia uno
    print("El número es par.")
else:
    print("El número es impar.")

cantidad = int(input("¿Cuántos números pares desea ver?: "))

contador = 0
i = 1

while contador < cantidad:  # aqui agregamos ':' al final de la linea
    if i % 2 == 0:
        print("Par número", contador + 1, ":", i)  # aqui separamos con comas todos los datos que estabn escritos fuera de las comillas
        contador += 1
    i += 1