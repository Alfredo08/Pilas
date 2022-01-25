from Node import Node
from Pila import Pila

pilaPersonas = Pila()

persona1 = Node( "Alex", "Martinez", 123 )
persona2 = Node( "Martha", "Sanchez", 456 )
persona3 = Node( "Alan", "Morales", 789 )

pilaPersonas.push( persona1 )
pilaPersonas.push( persona2 )
pilaPersonas.push( persona3 )


pilaPersonas.pop()
pilaPersonas.pop()
pilaPersonas.pop()

pilaPersonas.imprimePila()


# Crear una función que recibe como parámetro un string. Este string contiene una 
# fórmula matemática. La función debe de validar que los parentesis, corchetes y llaves
# sean correctos y tengan una estructura y orden válido. Retorna True si la validación 
# es exitosa, False de lo contrario
# ( x + y ) / ( z * 4 ) => True
# ( x + [z-3] * { 4 + 5 * (y - 7)} ) => True
# ( x + z / [ y * z) + 7 ) => False

