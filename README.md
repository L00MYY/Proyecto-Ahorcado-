Documentación del Juego del Ahorcado (Pygame)
Este proyecto consiste en una implementación del juego “Ahorcado” desarrollada en Python, utilizando la biblioteca Pygame para manejar gráficos, interacción con el usuario. La aplicación incluye un menú principal, una pantalla de carga y el funcionamiento completo del juego en una interfaz gráfica.
1. Uso de la aplicación
Para ejecutar la aplicación:
Instalar las dependencias necesaria (pygame).
Al iniciar la aplicación, se mostrará un menú con las siguientes opciones:
--Inicia el juego.
--Salir.
Durante el juego, el usuario debe ingresar letras utilizando el teclado (A–Z).
El sistema mostrará la palabra oculta, las letras incorrectas y el dibujo progresivo del ahorcado.
Al finalizar (ganar o perder), el usuario puede:
Presionar cualquier tecla para iniciar una nueva partida.
2. Librerías utilizadas
El proyecto utiliza las siguientes librerías:
• Pygame
Usada para la creación de la ventana, captura de eventos del teclado, renderizado de texto, dibujo del ahorcado y animaciones de la barra de carga.
Instalación:
pip install pygame
3. Versión funcional de Python
El programa ha sido probado y funciona correctamente en las siguientes versiones de Python:
Python 3.8
Python 3.9
Python 3.10
Python 3.11
4. Detalles relevantes sobre el funcionamiento
5. El dibujo del ahorcado se divide en seis etapas, correspondientes a los errores cometidos por el usuario.
El juego selecciona una palabra aleatoria de una lista interna predefinida.
Se utilizan funciones independientes para mantener una estructura modular:
Menú principal
Pantalla de carga
Lógica del juego
Sistema de dibujo del personaje
6. Componentes clave
main_menu_simple() en main.py
hangman_game(ventana) en game.py
draw_doll(SCREEN, doll_x, doll_y, wrong_count) en draw.py
wait_for_click() en main_menu_simple()
7. Funciones Clave
draw_text_centered(): Dibuja texto centrado en la ventana y devuelve su rectángulo para detección de clics.
draw_loading_screen(): Muestra la pantalla de carga con barra al 100% y mensaje para continuar.
main_menu_simple(): Controla el flujo completo del menú, detecta clics en las opciones y ejecuta las acciones correspondientes. wait_for_click(): Pausa la ejecución hasta que el usuario haga clic.
