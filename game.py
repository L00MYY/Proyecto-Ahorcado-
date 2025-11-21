import pygame
import random
from draw import draw_doll
from words import load_words, get_random_word
from sound import play_correct_sound, play_enter_sound, play_incorrect_sound, play_losing_sound, play_winning_sound


def hangman_game(ventana):

    #palabras = ["PYTHON", "PROGRAMACION", "PANTALLA", "AHORCADO", "JUEGO", "TECLADO"]

    words = load_words("words.txt")
    #print("Palabras cargadas:", words[:100], "...")
    word = get_random_word(words)

    letras_adivinadas = set()
    letras_incorrectas = set()
    intentos = 6

    font_letters = pygame.font.Font(None, 75)

    font_medium = pygame.font.Font(None, 36)
    font_large = pygame.font.Font(None, 50)

    reloj = pygame.time.Clock()
    jugando = True              
    game_over = False           # Estado final del juego

    while True:
        ventana.fill((30, 30, 30))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_over:
               # Volver a empezar si ya se terminó el juego
                if evento.type == pygame.KEYDOWN:
                    play_enter_sound()
                    # Volver a main
                    return  

            
            if jugando and evento.type == pygame.KEYDOWN:
                # rango entre letras de la A a la Z
                if pygame.K_a <= evento.key <= pygame.K_z:
                    letra = chr(evento.key).upper()

                    if letra in word:
                        letras_adivinadas.add(letra)
                        play_correct_sound()
                    else:
                        if letra not in letras_incorrectas:
                            letras_incorrectas.add(letra)
                            intentos -= 1
                            intentos = max(intentos, 0)  
                            play_incorrect_sound()

       
        mostrar = ""
        for letra in word:
            mostrar += letra + " " if letra in letras_adivinadas else "_ "

        texto_palabra = font_letters.render(mostrar, True, (255, 255, 255))
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

        x = 850
        y = 175
        draw_doll(ventana, x, y, intentos)

        
        if jugando:
            # Ganando
            if all(letra in letras_adivinadas for letra in word):
                jugando = False
                game_over = True
                play_winning_sound()

            # Perdiendo
            if intentos == 0:
                jugando = False
                game_over = True
                play_losing_sound()

    
        if game_over:
            if intentos > 0:
                msg = "¡GANASTE!"
                color = (0, 255, 0)
            else:
                msg = f"PERDISTE. La palabra era {word}"
                color = (255, 80, 80)

            texto_final = font_medium.render(msg, True, color)
            ventana.blit(texto_final, (80, 325))

            texto_restart = font_medium.render("Presiona cualquier tecla para volver al menú.", True, (200, 200, 200))
            ventana.blit(texto_restart, (80, 450))

        pygame.display.update()
        reloj.tick(60)
