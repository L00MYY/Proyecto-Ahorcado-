import pygame
import sys
import time
import os
from styles import TITLE_CHAR, SEPARATOR_CHAR, LOADING_CHAR, EMPTY_CHAR, center_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading_screen(total_steps=20, delay=0.1):
    clear_screen()
    
    title = "I N I C I A N D O   E L  J U E G O"
    print("\n" + center_text(TITLE_CHAR * len(title)))
    print(center_text(title))
    print(center_text(TITLE_CHAR * len(title)) + "\n")
    
    bar_length = 50
    
    print(center_text("CARGANDO DATOS..."))
    
    for step in range(total_steps + 1):
        progress = step / total_steps
        filled = int(bar_length * progress)
        unfilled = bar_length - filled
        
        bar = LOADING_CHAR * filled + EMPTY_CHAR * unfilled
        percent = int(progress * 100)
        
        output = center_text(f"[{bar}] {percent}%")
        print(output, end='\r')
        
        time.sleep(delay)

    print("\n" * 2 + center_text("¡Yay! Presiona Enter para continuar"))
    input()
    
def main_menu():
    while True:
        clear_screen()
        menu_title = "M E N U   P R I N C I P A L"
        
        print("\n" + center_text(SEPARATOR_CHAR * len(menu_title)))
        print(center_text(menu_title))
        print(center_text(SEPARATOR_CHAR * len(menu_title)) + "\n")

        options = [
            ("1", "Abrir el programa"),
            ("2", "Ver opciones"),
            ("3", "Acerca de..."),
            ("4", "Salir")
        ]
        
        for num, text in options:
            print(center_text(f"[{num}] - {text}"))

        print("\n" + center_text(SEPARATOR_CHAR * 30))
        
        choice = input(center_text("Ingresa tu opción: ")).strip()
        if choice == '1':
            print("\n[INFO] Abriendo el programa... (Presiona Enter para volver)")
            input()
        elif choice == '2':
            print("\n[INFO] Mostrando opciones... (Presiona Enter para volver)")
            input()
        elif choice == '3':
            print("\n[INFO] Información del autor: Yo. (Presiona Enter para volver)")
            input()
        elif choice == '4':
            print("\n[INFO] ¡Adiós! Nos vemos pronto.")
            time.sleep(1)
            break
        else:
            print("\n[ERROR] Opción inválida. Intenta un número del 1 al 4.")
            time.sleep(1)

if __name__ == "__main__":
    show_loading_screen()
    
    main_menu()