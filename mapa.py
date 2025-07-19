

class Mapa:

    def __init__(self):
        self.dimension = 5
        self.tablero = [["🔲" for _ in range (self.dimension)] for _ in range (self.dimension)]
        self.cantidad = self.dimension * 0,15



    def impirmir_tablero(self):
        for fila in self.tablero:
            print (''.join(fila))

mapa = Mapa()
mapa.impirmir_tablero()