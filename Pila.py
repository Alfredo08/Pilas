from Node import Node

class Pila:
    def __init__( self ):
        self.top = None
    
    def push( self, nuevoNodo ):
        if self.top != None:
            nuevoNodo.next = self.top
        self.top = nuevoNodo
    
    def imprimePila( self ):
        aux = self.top
        while aux != None:
            aux.imprimeDatos()
            aux = aux.next
    
    def pop( self ):
        aux = self.top
        if aux != None:
            self.top = aux.next
            aux.next = None
        
    def peek( self ):
        return self.top
        