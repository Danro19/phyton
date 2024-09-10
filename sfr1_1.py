#nV
#for i in range(0,nV)
#datos cc name y tpv vV
    #while cedula !=(-1)
        #3 if (variables Puerta a puerta%20  telemercado15  ejecutivo de ventas25) comisionVendedor
            #2 variables en if para credito y contado
# declara comicion de cada vendedor (individual)
#total ventas del mes 
#total de las comisiones entre los vendedores

nV = int(input("Ingrese el numero de vendedores activos: \n"))
cV_total = 0
vR_total = 0
vR_4Vent = 0 
for i in range(0, nV+1):
    name = input("Ingrese el nombre del vendedor: ")
    cc = input("Ingrese el numero de la cedula de ciudadania del vendedor: ")
    
    
    while cc != (-1):
        
        tpV= int(input("Ingrese el tipo de vendedor \n\
                     =============================\n\
                    |Puerta a puerta [1]          |\n\
                    |Telemercadeo[2]              |\n\
                    |Ejecutivo de ventas [3]):    |\n\
                     ============================= \n" ))
        vR=int(input("Ingrese el valor de las ventas realizadas en el mes (Pesos colombianos): "))
        cantidad_Clientes=int(input("Ingrese la cantidad de clientes de los vendedores:\n "))
        for i in range (0, cantidad_Clientes+1):    
            nameC=input("Ingrese el nombre del cliente: ")
            c_Cliente=input("Ingrese el codigo del cliente ")
            tpC= int(input("Ingrese el tipo de Venta \n\
                        =============================\n\
                        |Contado         [1]          |\n\
                        |Credito         [2]          |\n\
                        ============================= \n" ))
            if tpV == 1: 
                if tpC == 1:
                    comision=vR*0.25
                elif tpC==2:
                    comision=vR*0.20 
                else:
                    print("numero invalido")     
            elif tpV == 2:
                if tpC == 1:
                    comision=vR*0.15
                elif tpC==2:
                    comision=vR*0.10 
                print("numero invalido")     
            elif tpV == 3:
                if tpC == 1:
                    comision=vR*0.20
                elif tpC==2:
                    comision=vR*0.15 
                print("numero invalido") 
            else:
                print("numero invalido")    
            cV=comision
            vR_4Vent += vR
        print(f"El valor a pagar por comision es: {cV:,.0f}")
        cV_total += cV
        vR_total += vR
        
        break
    print("\n"*40)
    print(f"El valor total de las ventas del mes es: {vR_total:,.0f}")
    print(f"El valor total de las comisiones del mes es: {cV_total:,.0f}")
    print(f"El valor total de la venta  por cada vendedor es: {vR_4Vent:,.0f}")