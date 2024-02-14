import random

def baraja():
    return [(2, 'Picas'), (3, 'Picas'), (4, 'Picas'), (5, 'Picas'), (6, 'Picas'), (7, 'Picas'), (8, 'Picas'), (9, 'Picas'), (10, 'Picas'), ("Q", 'Picas'), ("J", 'Picas'), ("K", 'Picas'), ("A", 'Picas'),
            (2, 'Diamantes'), (3, 'Diamantes'), (4, 'Diamantes'), (5, 'Diamantes'), (6, 'Diamantes'), (7, 'Diamantes'), (8, 'Diamantes'), (9, 'Diamantes'), (10, 'Diamantes'), ("Q", 'Diamantes'), ("J", 'Diamantes'), ("K", 'Diamantes'), ("A", 'Diamantes'),
            (2, 'Corazones'), (3, 'Corazones'), (4, 'Corazones'), (5, 'Corazones'), (6, 'Corazones'), (7, 'Corazones'), (8, 'Corazones'), (9, 'Corazones'), (10, 'Corazones'), ("Q", 'Corazones'), ("J", 'Corazones'), ("K", 'Corazones'), ("A", 'Corazones'),
            (2, 'Tréboles'), (3, 'Tréboles'), (4, 'Tréboles'), (5, 'Tréboles'), (6, 'Tréboles'), (7, 'Tréboles'), (8, 'Tréboles'), (9, 'Tréboles'), (10, 'Tréboles'), ("Q", 'Tréboles'), ("J", 'Tréboles'), ("K", 'Tréboles'), ("A", 'Tréboles')]

def valor_carta(cartas):
    valor = sum([carta[0] if isinstance(carta[0], int) else 10 for carta in cartas])
    for carta in cartas:
        if carta[0] == 'A' and valor > 21:
            valor -= 10
    return valor

def mostrar(jugador, mano):
    print(f"El {jugador} tiene las siguientes cartas: {[carta[0] for carta in mano]} (total: {valor_carta(mano)})")

def blackjack():
    while True:
        deck = baraja()
        random.shuffle(deck)
        
        jugador = [deck.pop(), deck.pop()]
        maquina = [deck.pop(), deck.pop()]
        
        mostrar("Jugador", jugador)
        print(f"La primera carta de la máquina es: {maquina[0][0]} de {maquina[0][1]}")
        
        while True:
            if valor_carta(jugador) == 21:
                print("¡Blackjack! Has ganado")
                break
            elif valor_carta(jugador) > 21 and valor_carta(maquina) <= 21:
                print("Perdiste, te pasaste de 21.")
                break
            
            opcion = input("¿Quiere pedir otra carta? (s/n): ").lower()
            if opcion == 's':
                jugador.append(deck.pop())
                mostrar("Jugador", jugador)
            else:
                break
        
        while valor_carta(maquina) < 17:
            maquina.append(deck.pop())
        
        mostrar("Máquina", maquina)
        
        if valor_carta(maquina) > 21:
            print("La máquina se pasó de 21. Has ganado")
        elif valor_carta(jugador) > valor_carta(maquina) and valor_carta(jugador) <= 21:
            print("Has ganado")
        elif valor_carta(jugador) < valor_carta(maquina):
            print("La máquina ha ganado")
        else:
            if valor_carta(jugador) <= 21:
                print("Empate, nadie gana")

        opcion = input("¿Quiere jugar otra vez? (s/n): ").lower()
        if opcion != 's':
            break

blackjack()