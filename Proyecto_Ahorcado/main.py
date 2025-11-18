from styles import TITLE_CHAR, SEPARATOR_CHAR, LOADING_CHAR, EMPTY_CHAR, center_text

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
    
    main_menu()