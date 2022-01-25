class Node:
    def __init__( self, caracter ):
        self.caracter = caracter
        self.next = None

    def imprimeDatos( self ):
        print( self.caracter )