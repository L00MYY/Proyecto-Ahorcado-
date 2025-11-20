"""from styles import TITLE_CHAR, SEPARATOR_CHAR, LOADING_CHAR, EMPTY_CHAR, center_text

def show_loading_screen_instant(total_steps=20):
    title = "I N I C I A N D O   E L J U E G O"
    print("\n" + center_text(TITLE_CHAR * len(title)))
    print(center_text(title))
    print(center_text(TITLE_CHAR * len(title)) + "\n")
    
    bar_length = 50
    
    print(center_text("CARGANDO DATOS..."))
    
    percent = 100
    bar = LOADING_CHAR * bar_length 
    
    output = center_text(f"[{bar}] {percent}%")
    print(output)
    
    print("\n" * 2 + center_text("¡Carga Completa! Presiona Enter para continuar."))
    input()
    
def main_menu():
    while True:
        menu_title = "M E N U   P R I N C I P A L"
        
        print("\n" + center_text(TITLE_CHAR * 40)) 
        print(center_text(menu_title))
        print(center_text(SEPARATOR_CHAR * len(menu_title)) + "\n")

        options = [
            ("1", "Abrir el programa"),
            ("2", "Ver opciones"),
            ("3", "Acerca de"),
            ("4", "Salir")
        ]
        
        for num, text in options:
            print(center_text(f"[{num}] - {text}"))

        print("\n" + center_text(SEPARATOR_CHAR * 30))
        
        choice = input(center_text("Ingresa tu opción (1-4): ")).strip()
        
        print("\n" + SEPARATOR_CHAR * 80) 
        
        if choice == '1':
            print("\n Abriendo el programa... (Presiona Enter para volver)")
            input()
        elif choice == '2':
            print("\n Mostrando opciones... (Presiona Enter para volver)")
            input()
        elif choice == '3':
            print("\n Información del autor: Yo. (Presiona Enter para volver)")
            input()
        elif choice == '4':
            print("\n ¡Adiós! Nos vemos pronto.")
            break
        else:
            print("\n ERROR Opción inválida. Intenta un número del 1 al 4.")
            input("Presiona Enter para intentar de nuevo...")

if __name__ == "__main__":
    show_loading_screen_instant()
    
    main_menu()"""
    
    

"""import tkinter as tk
from tkinter import messagebox 

TITLE_CHAR = "="
SEPARATOR_CHAR = "-"
LOADING_CHAR = "#"

def center_text(text, width=80):
    padding = (width - len(text)) // 2
    return " " * padding + text + " " * (width - len(text) - padding)

root = None
content_frame = None
user_choice_var = None


def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_loading_screen_instant():
    global root, content_frame
    clear_frame()

    title = "I N I C I A N D O   E L  J U E G O"
    
    tk.Label(content_frame, text=center_text(TITLE_CHAR * len(title), 50), font=('Monospace', 12)).pack(pady=(20, 0))
    tk.Label(content_frame, text=center_text(title, 50), font=('Monospace', 14, 'bold')).pack()
    tk.Label(content_frame, text=center_text(TITLE_CHAR * len(title), 50), font=('Monospace', 12)).pack(pady=(0, 20))
    
    tk.Label(content_frame, text="CARGANDO DATOS...", font=('Monospace', 12)).pack(pady=10)
    
    bar_length = 50
    percent = 100
    bar = LOADING_CHAR * bar_length 
    output = center_text(f"[{bar}] {percent}%", 50)
    tk.Label(content_frame, text=output, font=('Monospace', 10)).pack(pady=5)
    
    tk.Label(content_frame, text="¡Carga Completa!", font=('Monospace', 12)).pack(pady=(30, 10))
    tk.Button(content_frame, text="Presiona para continuar", command=main_menu).pack()

def handle_menu_choice():
    choice = user_choice_var.get()
    
    if choice == '1':
        messagebox.showinfo("Programa", "Abriendo el programa...")
    elif choice == '2':
        messagebox.showinfo("Opciones", "Mostrando opciones...")
    elif choice == '3':
        messagebox.showinfo("Acerca de", "Información del autor: Yo.")
    elif choice == '4':
        messagebox.showinfo("Salir", "¡Adiós! Nos vemos pronto.")
        root.quit()
    else:
        messagebox.showerror("ERROR", "Opción inválida. Intenta un número del 1 al 4.")

    if choice != '4':
        user_choice_var.set("") 
        main_menu() 


def main_menu():
    global user_choice_var
    clear_frame()
    
    menu_title = "M E N U   P R I N C I P A L"
    
    tk.Label(content_frame, text=center_text(TITLE_CHAR * 40, 50), font=('Monospace', 12)).pack(pady=(20, 0)) 
    tk.Label(content_frame, text=center_text(menu_title, 50), font=('Monospace', 16, 'bold')).pack()
    tk.Label(content_frame, text=center_text(SEPARATOR_CHAR * len(menu_title), 50)).pack(pady=(0, 20))

    options = [
        ("1", "Abrir el programa"),
        ("2", "Ver opciones"),
        ("3", "Acerca de"),
        ("4", "Salir")
    ]
    
    for num, text in options:
        tk.Label(content_frame, text=center_text(f"[{num}] - {text}", 50), font=('Monospace', 12)).pack()

    tk.Label(content_frame, text=center_text(SEPARATOR_CHAR * 30, 50)).pack(pady=(20, 10))
    
    tk.Label(content_frame, text="Ingresa tu opción (1-4):", font=('Monospace', 10)).pack()
    
    user_choice_var = tk.StringVar()
    entry = tk.Entry(content_frame, textvariable=user_choice_var, justify='center', width=10)
    entry.pack(pady=5)
    
    entry.bind('<Return>', lambda event=None: handle_menu_choice())
    
    tk.Button(content_frame, text="Seleccionar", command=handle_menu_choice).pack(pady=10)
    entry.focus_set() 
    
def start_app():
    global root, content_frame
    
    root = tk.Tk()
    root.title("Menú de Juego")
    root.geometry("450x450")
    root.resizable(False, False)
    
    content_frame = tk.Frame(root, padx=20, pady=20)
    content_frame.pack(expand=True, fill='both')
    
    show_loading_screen_instant()
    
    root.mainloop()

if __name__ == "__main__":
    start_app()"""
    

import pygame
import sys
from game import hangman_game

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (52, 152, 219)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menú")

font_small = pygame.font.Font(None, 24)
font_medium = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 50)
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2


def draw_text_centered(text, font, color, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (center_x, y)
    screen.blit(textobj, textrect)
    return textrect


def draw_loading_screen():
    screen.fill(BLACK)
    
    title = "I N I C I A N D O   E L  J U E G O"
    draw_text_centered("=" * 30, font_small, WHITE, 50)
    draw_text_centered(title, font_large, YELLOW, 80)
    draw_text_centered("=" * 30, font_small, WHITE, 110)
    
    draw_text_centered("CARGANDO DATOS...", font_medium, WHITE, 180)
    
    bar_width = 300
    bar_height = 20
    bar_x = (SCREEN_WIDTH - bar_width) // 2
    bar_y = 220
    
    pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width, bar_height))
    draw_text_centered("100%", font_small, GREEN, bar_y + bar_height + 20)

    draw_text_centered("Carga Completa. Haz clic para continuar.", font_medium, WHITE, 300)
    
    pygame.display.flip()


def main_menu_simple():
    
    draw_loading_screen()
    
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_start = False
    
    
    options = [
        ("1", "Abrir el programa", "RUN"),
        ("2", "Acerca de", "ABOUT"),
        ("3", "Salir", "QUIT")
    ]
    
    button_rects = []
    
    y_start = 130
    padding = 40
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                for rect, target in button_rects:
                    if rect.collidepoint(mouse_pos):
                        if target == "QUIT":
                            running = False
                        elif target == "RUN":
                            #EJECUTAMOS
                            hangman_game(screen)
                        elif target == "OPTIONS":
                            draw_text_centered("Mostrando opciones... (Clic para volver)", font_medium, YELLOW, center_y)
                            pygame.display.flip()
                            wait_for_click()
                        elif target == "ABOUT":
                            draw_text_centered("Información: Yo. (Clic para volver)", font_medium, YELLOW, center_y)
                            pygame.display.flip()
                            wait_for_click()
        screen.fill(BLACK)

        menu_title = "M E N U   P R I N C I P A L"
        draw_text_centered("=" * 25, font_small, WHITE, 30)
        draw_text_centered(menu_title, font_large, BLUE, 60)
        draw_text_centered("-" * 25, font_small, WHITE, 90)

        button_rects = [] 
        
        for i, (num, text, target) in enumerate(options):
            full_text = f"[{num}] - {text}"
            
            rect = draw_text_centered(full_text, font_medium, WHITE, y_start + i * padding)
            button_rects.append((rect, target))
            
        draw_text_centered("-" * 20, font_small, WHITE, y_start + len(options) * padding)

        draw_text_centered("Haz clic en una opción.", font_small, WHITE, SCREEN_HEIGHT - 30)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def wait_for_click():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False

if __name__ == "__main__":
    main_menu_simple()