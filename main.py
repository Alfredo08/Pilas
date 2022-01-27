from cmath import pi
from Node import Node
from Pila import Pila

# Crear una función que recibe como parámetro un string. Este string contiene una 
# fórmula matemática. La función debe de validar que los parentesis, corchetes y llaves
# sean correctos y tengan una estructura y orden válido. Retorna True si la validación 
# es exitosa, False de lo contrario
# ( x + y ) / ( z * 4 ) => True
# ( x + [z-3] * { 4 + 5 * (y - 7)} ) => True
# ( x + z / [ y * z) + 7 ) => False

def validaExpresion( formula ):
    caracteres = Pila()
    for c in formula:
        if c == "(" or c == "[" or c == "{":
            nuevoNodo = Node( c )
            caracteres.push( nuevoNodo )
        if c == ")" or c == "]" or c == "}":
            tope = caracteres.peek()
            if (tope.caracter == "(" and c == ")") or (tope.caracter == "[" and c == "]") or (tope.caracter == "{" and c == "}"):
                caracteres.pop()
            else:
                return False
    if caracteres.top == None:
        return True
    else:
        return False

# print( validaExpresion( "( x + z / [ y * z) + 7 )" ) )

# Crear una función llamada aritméticaConPilas. La función recibe como parámetro un string.
# El string va a incluir números y operadores aritméticos. La funcion retorna el resultado
# de la operación aritmética si es que se puede evaluar. Retorna "No se puede evaluar" en caso
# de lo contrario.
#   5 10 + = 15
#   10 20 30 40 + + + = 100
#   5 10 20 + = "No se puede evaluar"
#   5 10 + + = "No se puede evaluar"  * / - +

def aritmeticaConPilas( formula ):
    arrSplit = formula.split()
    pilaNumeros = Pila()

    for x in arrSplit:
        if x == '+' or x == '-' or x == '*' or  x == '/':
            if pilaNumeros.longitud() >= 2:
                num1 = pilaNumeros.peek().caracter
                pilaNumeros.pop()
                num2 = pilaNumeros.peek().caracter
                pilaNumeros.pop()
                resultado = 0
                if x == '+':
                    resultado = num1 + num2
                if x == '-':
                    resultado = num2 - num1
                if x == '*':
                    resultado = num1 * num2
                if x == '/':
                    resultado = num2 / num1
                nuevoNodo = Node( resultado )
                pilaNumeros.push( nuevoNodo )
            else:
                return "No se puede evaluar la expresion."
        else:
            nuevoNodo = Node( int(x) )
            pilaNumeros.push( nuevoNodo )
    
    if pilaNumeros.longitud() == 1:
        return pilaNumeros.peek().caracter
    else:
        return "No se puede evaluar la expresion."


print( aritmeticaConPilas( "10 20 30 40 + + -" ) )