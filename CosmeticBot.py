#Bot para ventas de cosmeticos
#Impor os para poder limpiar la pantalla
import os

#Categorias
_Productos = "Productos"
_Maquillaje = "Maquillaje"
_cuidado_facial = "Cuidado Facial"
_cuidado_uñas = "Cuidado Uñas"
_accesorios = "Accesorios"

#productos filtrados por categoria
maquillaje = ["Base de maquillaje","Corrector","Polvo translúcido","Sombra de ojos","Delineador de ojos","Máscara de pestañas","Labial","Bronceador","Rubor"]
cuidado_facial = ["Desmaquillante","Crema hidratante facial","Tónico facial","Serum facial","Contorno de ojos","Protector solar facial"]
cuidado_uñas = ["Esmalte de uñas","Removedor de esmalte"]
accesorios = ["Cepillo para maquillaje","Esponja para maquillaje","Pinceles para ojos","Brochas para maquillaje"]
Productos_De_Maquillaje = ["Base de maquillaje $12.000","Corrector $8.000","Polvo translúcido $2.500","Sombra de ojos $9.000","Delineador de ojos $7.000","Máscara de pestañas $7.000","Labial $5.000","Bronceador $6.000","Rubor $3.500"]
Productos_De_cuidado_facial = ["Desmaquillante $4.500","Crema hidratante facial $19.000","Tónico facial $2.800","Serum facial $5.000","Contorno de ojos $19.000","Protector solar facial $12.000"]
Productos_De_cuidado_uñas = ["Esmalte de uñas $5.000","Removedor de esmalte $12.000"]
Productos_De_accesorios = ["Cepillo para maquillaje $4.400","Esponja para maquillaje $2.000","Pinceles para ojos $8.000","Brochas para maquillaje $7.000"]

#Precios
Precios = [12000,8000,2500,9000,7000,7000,5000,6000,3500,4500,19000,2800,5000,19000,12000,5000,12000,4400,2000,8000,70000]
Precios_De_Maquillaje = [12000,8000,2500,9000,7000,7000,5000,6000,3500]
Precios_De_cuidado_facial = [4500,19000,2800,5000,19000,12000]
Precios_De_cuidado_uñas = [5000,12000]
Precios_De_accesorios = [4400,2000,8000,70000]

#calculos
def Comprar(Categoria):
    entro = True
    while entro:
        if Categoria == _Productos:
            mostrar_productos_Compras(maquillaje + cuidado_facial + cuidado_uñas + accesorios , _Productos)
            Selecionado = int(input("Elija el producto que quiera comprar escribiendo el numero del producto: "))
            cantidad = int(input("¿Cuantas?: "))
            Total = CalculoDeVenta(Selecionado,cantidad,_Productos)
            print(f"El precio final es de {Total}")
            Opcion = input("Desea Realizar la compra? (S/N): ")
        elif Categoria == _Maquillaje:
            mostrar_productos_Compras(maquillaje, _Maquillaje)
            Selecionado = int(input("Elija el producto que quiera comprar escribiendo el numero del producto: "))
            cantidad = int(input("¿Cuantas?: "))
            Total = CalculoDeVenta(Selecionado,cantidad,_Maquillaje)
            print(f"El precio final es de {Total}")
            Opcion = input("Desea Realizar la compra? (S/N): ")
        elif Categoria == _cuidado_facial:
            mostrar_productos_Compras(cuidado_facial, _cuidado_facial)
            Selecionado = int(input("Elija el producto que quiera comprar escribiendo el numero del producto: "))
            cantidad = int(input("¿Cuantas?: "))
            Total = CalculoDeVenta(Selecionado,cantidad,_cuidado_facial)
            print(f"El precio final es de {Total}")
            Opcion = input("Desea Realizar la compra? (S/N): ")
        elif Categoria == _cuidado_uñas:
            mostrar_productos_Compras(cuidado_uñas, _cuidado_uñas)
            Selecionado = int(input("Elija el producto que quiera comprar escribiendo el numero del producto: "))
            cantidad = int(input("¿Cuantas?: "))
            Total = CalculoDeVenta(Selecionado,cantidad,_cuidado_uñas)
            print(f"El precio final es de {Total}")
            Opcion = input("Desea Realizar la compra? (S/N): ")
        elif Categoria == _accesorios:
            mostrar_productos_Compras(accesorios, _accesorios)
            Selecionado = int(input("Elija el producto que quiera comprar escribiendo el numero del producto: "))
            cantidad = int(input("¿Cuantas?: "))
            Total = CalculoDeVenta(Selecionado,cantidad,_accesorios)
            print(f"El precio final es de {Total}")
            Opcion = input("Desea Realizar la compra? (S/N): ")
        os.system('cls')
        if Opcion == "S" or Opcion == "s":
            print("Compra Realizada con exito")
            entro = False
            break
        elif Opcion == "N" or Opcion == "n":
            entro2 = True
            while entro2:
                Opcion2 = input("1 - Cancelar la compra\n2 - Volver a pedir\nIngrese el número de opción deseada: ")
                if Opcion2 == "1":
                    print("Compra Cancelada")
                    entro2 = False
                    entro = False
                    break
                elif Opcion2 == "2":
                    os.system('cls') 
                    entro2 = False
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        else:
                    print("Opción no válida. Intente de nuevo.")


def CalculoDeVenta(Selecionado,cantidad,nombre):
    if nombre == _Productos:
        if Selecionado > 0 and Selecionado <= len(Precios): 
            Total = Precios[Selecionado-1] * cantidad 
            return Total
        else:
            print("El numero que seleciono no es correcto. Intente de nuevo.")
            input("Presiona Enter para continuar...")
            os.system('cls') 
            Comprar(nombre)
    elif nombre == _Maquillaje:
        if Selecionado > 0 and Selecionado <= len(Precios_De_Maquillaje): 
            Total = Precios_De_Maquillaje[Selecionado-1] * cantidad 
            return Total
        else:
            print("El numero que seleciono no es correcto. Intente de nuevo.")
            input("Presiona Enter para continuar...")
            os.system('cls') 
            Comprar(nombre)
    elif nombre == _cuidado_facial:
        if Selecionado > 0 and Selecionado <= len(Precios_De_cuidado_facial): 
            Total = Precios_De_cuidado_facial[Selecionado-1] * cantidad 
            return Total
        else:
            print("El numero que seleciono no es correcto. Intente de nuevo.")
            input("Presiona Enter para continuar...")
            os.system('cls') 
            Comprar(nombre)
    elif nombre == _cuidado_uñas:
        if Selecionado > 0 and Selecionado <= len(Precios_De_cuidado_uñas): 
            Total = Precios_De_cuidado_uñas[Selecionado-1] * cantidad 
            return Total
        else:
            print("El numero que seleciono no es correcto. Intente de nuevo.")
            input("Presiona Enter para continuar...")
            os.system('cls') 
            Comprar(nombre)
    elif nombre == _accesorios:
        if Selecionado > 0 and Selecionado <= len(Precios_De_accesorios): 
            Total = Precios_De_accesorios[Selecionado-1] * cantidad 
            return Total
        else:
            print("El numero que seleciono no es correcto. Intente de nuevo.")
            input("Presiona Enter para continuar...")
            os.system('cls') 
            Comprar(nombre)

#submenues
def SubmenuProductos():
    while True:
        mostrar_productos(maquillaje + cuidado_facial + cuidado_uñas + accesorios , _Productos)
        print("")
        print("1. Ver Precios")
        print("2. Comprar")
        print("0. Volver")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            PreciosDelosProductos(Productos_De_Maquillaje +Productos_De_cuidado_facial + Productos_De_cuidado_uñas + Productos_De_accesorios, _Productos)
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Comprar(_Productos)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            menu_productos()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def Submenumaquillaje():
    while True:
        mostrar_productos(maquillaje, _Maquillaje)
        print("")
        print("1. Ver Precios")
        print("2. Comprar")
        print("0. Volver")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            PreciosDelosProductos(Productos_De_Maquillaje, _Maquillaje)
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Comprar(_Maquillaje)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            menu_productos()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def Submenucuidado_facial():
    while True:
        mostrar_productos(cuidado_facial,_cuidado_facial)
        print("")
        print("1. Ver Precios")
        print("2. Comprar")
        print("0. Volver")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            PreciosDelosProductos(Productos_De_cuidado_facial, _cuidado_facial)
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Comprar(_cuidado_facial)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            menu_productos()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def Submenucuidado_uñas():
    while True:
        mostrar_productos(cuidado_uñas, _cuidado_uñas)
        print("")
        print("1. Ver Precios")
        print("2. Comprar")
        print("0. Volver")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            PreciosDelosProductos(Productos_De_cuidado_uñas, _cuidado_uñas)
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Comprar(_cuidado_uñas)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            menu_productos()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def Submenuaccesorios():
    while True:
        mostrar_productos(accesorios, _accesorios)
        print("")
        print("1. Ver Precios")
        print("2. Comprar")
        print("0. Volver")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            PreciosDelosProductos(Productos_De_accesorios, _accesorios)
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Comprar(_accesorios)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            menu_productos()
            break
        else:
            print("Opción no válida. Intente de nuevo.")


#Listados de productos
def PreciosDelosProductos(Lista_Productos_Precios, nombre):
    if nombre == _Productos:
        print("------ Productos-------")
        for producto in Lista_Productos_Precios:
            print("- ", producto)
    else:
        print("------ Productos de", nombre, "-------")
        for producto in Lista_Productos_Precios:
            print("- ", producto)

def mostrar_productos(categoria, nombre):
    if nombre == _Productos:
        print("------ Productos-------")
        for producto in categoria:
            print("- ", producto)
    else:
        print("------ Productos de", nombre, "-------")
        for producto in categoria:
            print("- ", producto)

def mostrar_productos_Compras(categoria, nombre):
    contT = 0
    contC = 0
    if nombre == _Productos:
        print("------ Productos-------")
        for producto in categoria:
            contT += 1
            print(f"{contT} ", producto)
    else:
        print("------ Productos de", nombre, "-------")
        for producto in categoria:
            contC +=1
            print(f"{contC} ", producto)

#Menu principal
def menu_productos():
    Entro = True
    while Entro:
        print("------ Menú de Productos -------")
        print("1. Ver todos los Productos")
        print("2. Productos de Maquillaje")
        print("3. Productos de Cuidado facial")
        print("4. Productos de cuidado uñas")
        print("5. Productos de accesorios")
        print("0. Salir")
        opcion = input("Ingrese el número de opción deseada: ")
        os.system('cls') 
        if opcion == '1':
            SubmenuProductos()
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif opcion == '2':
            Submenumaquillaje()
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '3':
            Submenucuidado_facial()
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '4':
            Submenucuidado_uñas()
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '5':
            Submenuaccesorios()
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif opcion == '0':
            print("¡Hasta luego!")
            Entro = False
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    Nombre = input("Ingrese su nombre: ")
    os.system('cls') 
    print(f"Hola {Nombre} Bienvenido a CosmeticBot!")
    menu_productos()
    
# Llama a la función main para ejecutar el menú
main()




