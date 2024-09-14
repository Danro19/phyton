#datos que nos vamos a necesitar: n de estudiantes, codigo, nombre, nota1, nota2, nota3 (input)
#datos que vamos a entregar: la nota definitiva, aprovo o reprobo(output)
# #CONDICION PARA APROBAR, PROMEDIO MAYOR A 3.0, CALIFICACION MAX 5.0.
# VALOR DE CADA NOTA
# NOTA1 30%, NOTA2 30%, NOTA3 40%
# EL PROGRAMA SE TERMINA CUANDO EL CODIGO SEA 999 (USO DE WHILE O BREAK)  


dCalificacion={1:0.30, 2:0.30, 3:0.40}

n=int(input("Ingrese la cantidad de estudiantes: "))

estudiante={}
suma=0
for i in range(n):
    print(f"\nEstudiante {i+1} ")
    codigo = input("Codigo del estudiante ")
    dDatos = {}
    dDatos["nombre"]=input("Nombre? ")
    for j in range(3):
        dDatos[f"nota{j+1}"] = float(input(f"Ingrese la nota{j+1}: "))
    fNota=dCalificacion{1}*dDatos["nota1"]
    fNota2=dCalificacion{2}*dDatos["nota2"]
    fNota3=dCalificacion{3}*dDatos["nota3"]
    dDatos["calificacion"] = dCalificacion [dDatos["categoria"]] * dDatos["horas_lab"]

    docentes[cedula]=dDatos 
    suma += dDatos["honorarios"]