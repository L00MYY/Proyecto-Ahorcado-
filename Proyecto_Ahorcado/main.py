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
    
    

import tkinter as tk
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
    start_app()