#crear un archivo tipo .txt con diferentes variables(linea por palabra, termina en blanco al final del archivo)
#leer la palabra en la lista
#mirar si la palabra es palíndromo  *funcion reverse:*
#",".join (funcion separar con) no espacios
#pasar a minuscula .lower
#llamar a la funcion



def is_palindrome(s):
    reverse = s [::-1]
    if (s== reverse):
        return True
    return False

lstTF=[]
cp=int(input("Ingrese la cantidad de variables a introducir "))
for i in range(cp):
    n=(input(f"Ingrese una palabra {i+1}: ")).lower()
    if is_palindrome(n):
        lstTF.append("true") 
    else:
        lstTF.append("false")
    if n == "":
        break

print(",".join(lstTF))
