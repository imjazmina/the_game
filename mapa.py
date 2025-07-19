import random

class Mapa:


    def __init__(self, dimension=10):
        self.dimension = dimension
        self.tablero = [["🔲" for _ in range(self.dimension)] for _ in range(self.dimension)]
        #aca cre una matriz de boleanos false para despues condicionar los obstaculos
        self.obstaculo = [[False for _ in range(self.dimension)] for _ in range(self.dimension)]

    def imprimir_tablero(self):
        # print(f"\n🌟 Nivel {nivel} - Obstáculos: {cantidad_obstaculos}")
        for fila in self.tablero:
            print(''.join(fila))

class Nivel(Mapa):
    
    def __init__(self):
        super().__init__()
        # self.nivel = numero_nivel
        self.cantidad = 10
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
                #aca marco a true los obstaculos
                self.obstaculo[fila][col] = True
                colocados += 1

class Pieza:
    def __init__(self, x, y, simbolo):
        self.x = x
        self.y = y
        self.simbolo = simbolo
    
    def mover(self, direccion, mapa):
        delta_x, delta_y = 0,0
        if direccion == 'W': delta_x = -1
        elif direccion == 'S': delta_x = 1
        elif direccion == 'A': delta_y = -1
        elif direccion == 'D': delta_y = 1
        
        nuevo_x = self.x + delta_x
        nuevo_y = self.y + delta_y
        if 0 <= nuevo_x < mapa.dimension and 0 <= nuevo_y < mapa.dimension and not mapa.obstaculo[nuevo_x][nuevo_y]:
           
           mapa.tablero[self.x][self.y]  = "🔲"
           self.x, self.y = nuevo_x, nuevo_y
        #procedemos a crear el nuevo simbolo
           mapa.tablero[self.x][self.y] = self.simbolo

        else:
            print("Movimiento invalido, te estas yendo del mapa")
    
class Jugador(Pieza):
    def __init__(self, x, y):
        super().__init__(x, y, 'P')  # usa constructor de Pieza para no repetir del codigo acordate
        self.nivel = 1

    def capturar(self, npc):
        return self.x == npc.x and self.y == npc.y

class NPC(Pieza):
    def __init__(self, x, y, nombre, historia_es, historia_gua, trivia):
        super().__init__(x, y, 'M')  # usa constructor de Pieza para no repetir codigo, y luego agrega sus propios atributos
        self.nombre = nombre
        self.historia_es = historia_es
        self.historia_gua = historia_gua
        self.trivia = trivia
        self.capturado = False
       
mapa = Nivel()
# mapa.imprimir_tablero()
# Creamos el jugador y lo colocamos en el mapa
jugador = Jugador(0, 0)
mapa.tablero[jugador.x][jugador.y] = jugador.simbolo

# Creamos un NPC y lo colocamos en el mapa
npc = NPC(
    2, 2,
    "Teju Jagua",
    "Es un ser mitad lagarto y mitad perro que guarda tesoros.",
    "Peteĩ mymba teju ha jagua rehegua, ombyaty mba’e reraháva.",
    (
        "¿Cuál es el mito con cuerpo de lagarto y cabeza de perro?",
        ["Pombero", "Teju Jagua", "Luisón"],
        2  # Opción correcta
    )
)
mapa.tablero[npc.x][npc.y] = npc.simbolo

# Bucle principal del juego
while True:
    mapa.imprimir_tablero()
    direccion = input("Mover (WASD): ").upper()
    jugador.mover(direccion, mapa)
    
    #poner la conidicion de que no se puede mover al obtaculo

    if jugador.capturar(npc) and not npc.capturado:
        print(f"\n📖 Historia de {npc.nombre}")
        print(f"🇪🇸 {npc.historia_es}")
        print(f"🇬🇺 {npc.historia_gua}")
        
        pregunta, opciones, correcta = npc.trivia
        print("\n❓", pregunta)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        
        respuesta = int(input("Elige la opción correcta (1/2/3): "))
        if respuesta == correcta:
            print("✅ ¡Correcto! Pasaste de nivel.")
            npc.capturado = True
            break
        else:
            print("❌ Incorrecto. Intentá de nuevo.")
