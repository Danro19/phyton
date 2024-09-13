cadena= "mi cadena de phyton"


#METODOS para trabajar con cambio de mayusculas a minusculas
print(cadena.capitalize())#mayusculas inicial
print(cadena.lower())#minusculas total
print(cadena.upper())#mayusculas total
print(cadena.swapcase())#intercambia las mayus a minus
print(cadena.title())#la va a separar por palabras, y pone mayus la inical



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# METODOS para buscar y reemplazar caracterers
print(cadena.count("a")) #cuenta secuencias de cadenas (repeticion de cadenas) primer lugar, es para la secuencia, la segunda y tercera son rangos
print(cadena.startswith("mi")) #Lector de prefijos y subcadenas, al iguan que count, se puede poner rangos pone true o false
print(cadena.endswith("phyton"))#lector de sufijos. pone true o false
print(cadena.find("de")) #busca subcadenas e imprime el lugar donde esta, las cadenas inician en 0, entonces llegado el caso no encuentre la cadena devolvera un numero inferior a cero, tambien se puede usar rangos 
#>>>>****Tanto en index como en find con al añadir r al inicio se empieza a buscar de la derecha******<<<<
print(cadena.rindex("de"))#realiza la misma tarea que find, pero en este caso arrojara una excepcion y el programa se detendra de forma abructa (preguntar en clases)  


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#METODOS para clasificar caracteres de una cadena
print("abc123".isalnum())#devuelve True si es una cadena alfanumerica, false si tiene caracteres especiales
print("abc".isalpha())#devuelve true si es una cadena de alfabetica, false si tiene otro caracter diferente
print("123".isdigit())#devuelve true si es una cadena numerica, devuelve false si tiene caracteres diferentes
print("abc1587?".islower())#devuelve true si todas las letra son minusculas, devuelve false si hay letras mayusculas, no influye que haya numeros o caracteres
print("abc".isupper())#devuelve true si todas las letra son Mayusculas, devuelve false si hay letras minusculas, no influye que haya numeros o caracteres
print("Python Es Genial".istitle())#Revisa palabra por palabra y mira si esta capitalizada(mayuscula inicial) y devuelve True si se cumple eso, de lo contrario devolvera un false