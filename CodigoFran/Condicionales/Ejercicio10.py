"""La pizzería Bella Napoli ofrece pizzas vegetarianas y
no vegetarianas a sus clientes. Los ingredientes para
cada tipo de pizza aparecen a continuación.

    Ingredientes vegetarianos: Pimiento y tofu
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una
pizza vegetariana o no, y en función de su respuesta le
muestre un menú con los ingredientes disponibles para que
elija. Solo se puede eligir un ingrediente además de la
mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida
es vegetariana o no y todos los ingredientes que lleva."""

pizza = input("¿Quiere una pizza Vegetariana?(SI/NO): ")

if pizza == "SI":
    print("Los ingredientes disponibles son: ")
    print("-Pimiento")
    print("-Tofu")

    ingrediente = input("Introduce un ingrediente de los ofertados: ")
    if ingrediente == "Pimiento" or ingrediente == "Tofu":
        print("La pizza es Vegetariana")
        print("Los ingredientes son:")
        print("-Tomate")
        print("-Mozarella")
        print(f"-{ingrediente}")
    else:
        print("El ingrediente Introducido es incorrecto")
else:
    print("Los ingredientes disponibles son: ")
    print("-Peperoni")
    print("-Jamon")
    print("-Salmon")

    ingrediente = input("Introduce un ingrediente de los ofertados: ")
    if ingrediente == "Peperoni" or ingrediente == "Jamon" or ingrediente == "Salmon":
        print("La pizza no es Vegetariana")
        print("Los ingredientes son:")
        print("-Tomate")
        print("-Mozarella")
        print(f"-{ingrediente}")
    else:
        print("El ingrediente Introducido es incorrecto")
