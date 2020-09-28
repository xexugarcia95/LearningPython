"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a
continuación.

    -Ingredientes vegetarianos: Pimiento y tofu.
    -Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
o no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija. Solo se puede eligir un ingrediente además de
la mozzarella y el tomate que están en todas la pizzas. Al final se debe
mostrar por pantalla si la pizza elegida es vegetariana o no y todos lo
ingredientes que lleva."""

pizza = input("Elige tu pizza: ")

if pizza == "vegetariana":
    print("Ingredientes: Pimiento y tofu.")
    v = input("Elige...")
    print("Tu pizza vegetariana contiene: " + v + ",mozzarella y tomate")
else:
    print("Ingredientes: Peperoni, Jamón y Salmón")
    v = input("Elige...")
    print("Tu pizza no vegetariana contiene: " + v + ",mozzarella y tomate")
