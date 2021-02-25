INFINITO = float('Inf')
def calcularAreaHorizontal(largo, ancho):
    area= largo*ancho
    return area
def calcularVolumen(area, altura):
    volumen= area*altura
    return volumen
def tiposPartes(nomParte):
    #Si se modifican las categorias, recordar modificar el numero al final
    print("Ingrese el numero que coincida con el tipo de la parte " + nomParte + "\n")
    print("0. Piezas que requieren resistencia mecanica")
    print("1. Piezas con geometrias curvas que requieren estetica")
    print("2. Contenedor de circuitos.")
    print("3. Repuestos para impresoras CAP")
    print("4. Piezas articuladas")
    print("5. Piezas delicadas (soportes para circuitos o pequeños)")
    cantidadTiposDePartes= 6
    return cantidadTiposDePartes
def organizarPartesCategoria(cantidadTiposDePartes):
    global partes
    partesPorTipo= [[] for _ in range(cantidadTiposDePartes)]
    for i in range(cantidadTiposDePartes):
        for j in partes:
            tipoParte=partes[j][3]
            if(i==tipoParte):
                partesPorTipo[i].append(j)
    return partesPorTipo

def agendamientoCamas(bins,s):
    camasOrdenadas=sorted(bins.keys(), key = lambda x: bins[x][1])
    ans,N = [],len(camasOrdenadas)
    f=s
    for bin in camasOrdenadas:
        si=f
        si=si%24
        ti=bins[bin][2]
        fi=f+ti
        fi=fi%24
        f=fi
        ans.append([bin, bins[bin][0], si, fi])
    return ans
def ocupadoBin(bin, partes):
    """
    Calcula cuan ocupado esta un bin en el momento actual
    """
    ocupado = 0
    for parte in bin[0]:
        ocupado += partes[parte][8]
    return ocupado
def encontrartiCama(bin, partes):
    ti=0
    for i in bin[0]:
        ti+= partes[i][7]
    return ti
def bestFit(sizeBin, bins, partes, ordenados):
    for j in ordenados:
        flag=0
        restante2= INFINITO
        for bin in bins:
            ocupacion = ocupadoBin(bins[bin], partes)
            pesoTrabajo=partes[j][8]
            restante=sizeBin-ocupacion-pesoTrabajo
            tiActualCama= encontrartiCama(bins[bin], partes)
            tiParte= partes[j][7]
            if(restante>=0):
                #print("Si cabe", j, "pesa" ,pesoTrabajo, "en", bin + "." , "Hay de ocupacion", ocupacion, "y queda" , restante)
                if((restante<restante2) and ((tiActualCama + tiParte)<= bins[bin][1]) and ((tiActualCama + tiParte)<= partes[j][6])):
                    flag=1
                    restante2=restante
                    binSeleccionado= bin
                    #print("el bin seleccionado es", binSeleccionado)
        if(flag==1):
            bins[binSeleccionado][0].append(j)
            bins[binSeleccionado][1]= min(bins[binSeleccionado][1], partes[j][6])
            bins[binSeleccionado][2]= encontrartiCama(bins[binSeleccionado], partes)
            #print("Se agrega el parte", j, "al bin", binSeleccionado)
            #print(bins)
        elif(flag==0):
            name="B"+str(len(bins)+1)
            bins[name]=[[j], partes[j][6], partes[j][7]]
            ocupacion = ocupadoBin(bins[name], partes)
            #print("Se crea el bin", name, "y su ocupacion es", ocupacion)
    return bins      
def main():
    global partes
    quemado=int(input("Desea que se ejecute el sistema por defecto?\n0 No\n1 Si\n"))
    if(quemado==1):
        #partes["Ji"]=[... , ( largoi, anchoi, altoi, tipoi, areai, voli, di, ti, wi), ...]
        partes=dict()
        partes["J1"]=[1, 1, 1, 1, 1, 1, 5, 2, 0.5]
        partes["J2"]=[1, 1, 1, 1, 1, 1, 3, 1, 0.7]
        partes["J3"]=[1, 1, 1, 1, 1, 1, 6, 3, 0.5]
        partes["J4"]=[1, 1, 1, 1, 1, 1, 1, 1, 0.2]
        partes["J5"]=[1, 1, 1, 1, 1, 1, 1, 1, 0.4]
        partes["J6"]=[1, 1, 1, 1, 1, 1, 8, 6, 0.2]
        partes["J7"]=[1, 1, 1, 1, 1, 1, 5, 3, 0.5]
        partes["J8"]=[1, 1, 1, 1, 1, 1, 7, 2, 0.1]
        partes["J9"]=[1, 1, 1, 1, 1, 1, 7, 4, 0.6]
    elif(quemado==0):
        cantidadPartes=int(input("Ingrese la cantidad de partes a imprimir\n"))
        partes=dict()
        for i in range(cantidadPartes):
            nomParte=str(input("Ingrese el nombre de la parte " + str(i+1)+ "\n"))
            largoParte=float(input("Ingrese la longitud de la parte " + nomParte + "\n"))
            anchoParte=float(input("Ingrese el ancho de la parte " + nomParte + "\n"))
            alturaParte=float(input("Ingrese la altura de la parte " + nomParte + "\n"))
            cantidadTiposDePartes = tiposPartes(nomParte)
            tipoParte=int(input(""))
            areaParte= calcularAreaHorizontal(largoParte, anchoParte)
            volumenParte= calcularVolumen(areaParte, alturaParte)
            plazoEntregaParte=float(input("Ingrese el plazo de entrega de la parte " + nomParte + "\n"))
            tiempoEjecucionParte=float(input("Ingrese el tiempo de ejecucion de la parte " + nomParte + " (Recuerde que este valor lo da CURA)\n"))
            if(tiempoEjecucionParte>=plazoEntregaParte):
                print("No se puede ingresar una parte que su tiempo de ejecucion sea mayor al plazo de entrega")
                return
            weightParte=float(input("Ingrese el peso de la parte " + nomParte + " (Este valor se obtiene mientras el proyecto se toma unidimensional)\n"))
            parte=[largoParte, anchoParte, alturaParte, tipoParte, areaParte, volumenParte, plazoEntregaParte, tiempoEjecucionParte, weightParte]
            partes[nomParte] = parte
        #print(organizarPartesCategoria(partes, cantidadTiposDePartes))
    sizeBin=1
    bins=dict()
    partes2=sorted(partes.keys(), key = lambda x: partes[x][8], reverse=True)
    bins = bestFit(sizeBin, bins,partes,partes2)
    camasOrdenadas=agendamientoCamas(bins, 7)
    print(camasOrdenadas)
main()
