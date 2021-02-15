def calcularAreaHorizontal(largo, ancho):
    area= largo*ancho
    return area

def calcularVolumen(area, altura):
    volumen= area*altura
    return volumen

def tiposPartes():
    #Si se modifican las categorias, recordar modificar el numero al final
    print("0. Piezas que requieren resistencia mecanica")
    print("1. Piezas con geometrias curvas que requieren estetica")
    print("2. Contenedor de circuitos.")
    print("3. Repuestos para impresoras CAP")
    print("4. Piezas articuladas")
    print("5. Piezas delicadas (soportes para circuitos o pequeños)")
    cantidadTiposDePartes= 6
    return cantidadTiposDePartes

def organizarPartesCategoria(partes, cantidadTiposDePartes):
    partesPorTipo= [[] for _ in range(cantidadTiposDePartes)]
    for i in range(cantidadTiposDePartes):
        for j in partes:
            tipoParte=partes[j][4]
            if(i==tipoParte):
                partesPorTipo[i].append(j)
    return partesPorTipo
                
            
def main():
    cantidadPartes=int(input("Ingrese la cantidad de partes a imprimir\n"))
    partes=dict()
    for i in range(cantidadPartes):
        nomParte=str(input("Ingrese el nombre de la parte " + str(i+1)+ "\n"))
        largoParte=float(input("Ingrese la longitud de la parte " + nomParte + "\n"))
        anchoParte=float(input("Ingrese el ancho de la parte " + nomParte + "\n"))
        alturaParte=float(input("Ingrese la altura de la parte " + nomParte + "\n"))
        plazoEntregaParte=float(input("Ingrese el plazo de entrega de la parte " + nomParte + "\n"))
        print("Ingrese el numero que coincida con el tipo de la parte " + nomParte + "\n")
        cantidadTiposDePartes = tiposPartes()
        tipoParte=int(input(""))
        areaParte= calcularAreaHorizontal(largoParte, anchoParte)
        volumenParte= calcularVolumen(areaParte, alturaParte)
        parte=[largoParte, anchoParte, alturaParte, plazoEntregaParte, tipoParte, areaParte, volumenParte]
        partes[nomParte] = parte
    print(organizarPartesCategoria(partes, cantidadTiposDePartes))
    
main()
