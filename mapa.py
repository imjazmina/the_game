import random

class Mapa:

    def __init__(self, dimension=10):
        self.dimension = dimension
        self.tablero = [["🔲" for _ in range(self.dimension)] for _ in range(self.dimension)]

    def imprimir_tablero(self, nivel, cantidad_obstaculos):
        # print(f"\n🌟 Nivel {nivel} - Obstáculos: {cantidad_obstaculos}")
        for fila in self.tablero:
            print(''.join(fila))


class Nivel(Mapa):
    
    def __init__(self, numero_nivel=7):
        super().__init__()
        self.nivel = numero_nivel
        self.cantidad = 3 + (self.nivel - 1) * 2
        self.colocar_obstaculos()

    def colocar_obstaculos(self):
        colocados = 0
        while colocados < self.cantidad:
            fila = random.randint(0, self.dimension - 1)
            col = random.randint(0, self.dimension - 1)

            if (fila, col) in [(0, 0), (self.dimension - 1, self.dimension - 1)]:
                continue

            if self.tablero[fila][col] == "🔲":
                self.tablero[fila][col] = "⛔"
                colocados += 1


# # Crear y mostrar los 7 niveles con dificultad creciente
# for i in range(1, 8):
#     nivel = Nivel(i)
#     nivel.imprimir_tablero(nivel.nivel, nivel.cantidad)

nivel = Nivel()
nivel.imprimir_tablero(nivel.nivel, nivel.cantidad)



