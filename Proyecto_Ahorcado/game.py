import pygame
import random
from draw import draw_doll

PALABRAS = ["PYGAME", "AHORCADO", "JUEGO", "PROGRAMACION", "EQUIPO"]

def hangman_game(ventana):

    # ----------------------
    # Palabra aleatoria
    # ----------------------
    palabras = ["PYTHON", "PROGRAMACION", "PANTALLA", "AHORCADO", "JUEGO", "TECLADO"]
    palabra = random.choice(palabras)

    letras_adivinadas = set()
    letras_incorrectas = set()
    intentos = 6

    font_medium = pygame.font.Font(None, 36)
    font_large = pygame.font.Font(None, 50)

    reloj = pygame.time.Clock()
    jugando = True              # Para evitar seguir escribiendo al perder o ganar
    game_over = False           # Estado final del juego

    while True:
        ventana.fill((30, 30, 30))

        # ----------------------
        # EVENTOS
        # ----------------------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_over:
                # Si ya terminó la partida, presionar cualquier tecla reinicia
                if evento.type == pygame.KEYDOWN:
                    return  # Regresa a main() para iniciar otra vez

            # SOLO acepta letras si aún está jugando
            if jugando and evento.type == pygame.KEYDOWN:
                if pygame.K_a <= evento.key <= pygame.K_z:
                    letra = chr(evento.key).upper()

                    if letra in palabra:
                        letras_adivinadas.add(letra)
                    else:
                        if letra not in letras_incorrectas:
                            letras_incorrectas.add(letra)
                            intentos -= 1
                            intentos = max(intentos, 0)  # Para que NO llegue a negativo

        # ----------------------
        # DIBUJAR PALABRA
        # ----------------------
        mostrar = ""
        for letra in palabra:
            mostrar += letra + " " if letra in letras_adivinadas else "_ "

        texto_palabra = font_large.render(mostrar, True, (255, 255, 255))
        ventana.blit(texto_palabra, (80, 100))

        # Letras incorrectas
        texto_incorrectas = font_medium.render(
            "Incorrectas: " + " ".join(letras_incorrectas),
            True,
            (255, 100, 100)
        )
        #                                 POSICIÓN
        ventana.blit(texto_incorrectas, (80, 160))

        # Intentos restantes
        texto_intentos = font_medium.render(f"Vidas: {intentos}", True, (200, 180, 0))
        ventana.blit(texto_intentos, (80, 220))

        # ----------------------
        # Dibujar muñeco según vidas
        # ----------------------
        x = 600
        y = 200
        draw_doll(ventana, x, y, intentos)

        # ----------------------
        # CONDICIONES DE FIN
        # ----------------------
        if jugando:
            # GANÓ
            if all(letra in letras_adivinadas for letra in palabra):
                jugando = False
                game_over = True

            # PERDIÓ
            if intentos == 0:
                jugando = False
                game_over = True

        # ----------------------
        # MENSAJE FINAL
        # ----------------------
        if game_over:
            if intentos > 0:
                msg = "¡GANASTE!"
                color = (0, 255, 0)
            else:
                msg = f"PERDISTE. La palabra era {palabra}"
                color = (255, 80, 80)

            texto_final = font_medium.render(msg, True, color)
            ventana.blit(texto_final, (80, 325))

            texto_restart = font_medium.render("Presiona cualquier tecla para jugar de nuevo", True, (200, 200, 200))
            ventana.blit(texto_restart, (120, 450))

        pygame.display.update()
        reloj.tick(60)
