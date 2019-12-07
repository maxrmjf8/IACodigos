#Code in Class 
#Ejercicio 1.- Programa en python que dado como dato el sueldo de un trabajador, le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y del 12% en caso contrario.
def main():
    st= float(input("Introduce tu sueldo: "))
    if(st<1000):
        sf = st*.15 + st
    elif(st >= 1000):
        sf= st*.12+st
    
    print("El sueldo final es: ", sf)

if __name__ == "__main__":
    main()

#Ejercicio 2.- Programa que dado como datos la categoría y el sueldo de un trabajor, calcule el aumento correspondiente teniendo en cuenta la siguiente información e imprima el nuevo sueldo del trabajador:
#Categoría 1 : Aumento 15%
#Categoría 2 : Aumento 10%
#Categoría 3 : Aumento 8%
#Categoría 4 : Aumento 7%

def main():
    ciclo =  True
    while (ciclo==True):
        print("Trabajador")
        print("Categoría 1, Categoría 2, Categoría 3, Categoría 4")
        TT= int(input("¿Cuál es la clase de trabajador que es? "))
        ST= float(input("Ingrese su sueldo: "))

        if(TT==1):
            sf= ST*.15+ST
            print("El sueldo final es: ", sf)
        elif(TT==2):
            sf= ST*.10+ST
            print("El sueldo final es: ", sf)
        elif(TT==3):
            sf= ST*.08+ST
            print("El sueldo final es: ", sf)
        elif(TT==4):
            sf= ST*.07+ST
            print("El sueldo final es: ", sf)
        else:
            print("Valor inválido")
        opc=input("¿Desea ingresar otro trabajador? (Y/N)")
        if (opc== "Y" or opc== "y"):
            ciclo=True
        else:
            ciclo=False
if __name__ == "__main__":
    main()