#nV
#for i in range(0,nV)
#datos cc name y tpv vV
    #while cedula !=(-1)
        #3 if (variables Puerta a puerta%20  telemercado15  ejecutivo de ventas25) comisionVendedor
# declara comicion de cada vendedor (individual)
#total ventas del mes 
#total de las comisiones entre los vendedores


nV = int(input("Ingrese el numero de vendedores activos: \n"))
cV_total = 0
vR_total = 0
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
        if tpV == 1:
                comision=vR*0.20
        elif tpV == 2:
                comision=vR*0.15
        elif tpV == 3:
                comision=vR*0.25
        else:
            print("numero invalcco")    
        cV=comision
        print(f"El valor a pagar por comision es: {cV:,.0f}")
        cV_total += cV
        vR_total += vR
        break
    print("\n"*40)

print(f"El valor total de las ventas del mes es: {vR_total:,.0f}")
print(f"El valor total de las comisiones del mes es: {cV_total:,.0f}")