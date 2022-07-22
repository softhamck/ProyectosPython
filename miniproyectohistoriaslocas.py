#Historias Locas
#Mad Libs

palabra1 = input('Ingrese una parte del cuerpo en singular: ')
palabra2 = int(input('Ingrese un numero: '))
palabra3 = input('Ingrese un órgano en singular: ')

print("\n Esta es tu historia loca:")
print("\n La {} está formada principalmente por {} huesos y cavidades en las que se encuentran órganos como el {} y los sentidos.".format(palabra1, palabra2, palabra3))

horginial = input("\nQuieres ver la historia original? y = si, n = not: ")

if horginial== "y":
    print("\nEsta es la historia original: ")
    print("La cabeza está formada principalmente por 14 huesos y cavidades en las que se encuentran órganos como el cerebro y los sentidos")
else:
    print("El programa terminó")
