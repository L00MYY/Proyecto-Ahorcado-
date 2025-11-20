Documentación del Juego del Ahorcado (Pygame)
Este proyecto consiste en una implementación del juego “Ahorcado” desarrollada en Python, utilizando la biblioteca Pygame para manejar gráficos, interacción con el usuario y animaciones. La aplicación incluye un menú principal, una pantalla de carga y el funcionamiento completo del juego en una interfaz gráfica.
1. Uso de la aplicación
Para ejecutar la aplicación:
Instalar las dependencias necesaria (pygame).
Al iniciar la aplicación, se mostrará un menú con las siguientes opciones:
ENTER: Inicia el juego.
ESC: Cierra la aplicación.
Durante el juego, el usuario debe ingresar letras utilizando el teclado (A–Z).
El sistema mostrará la palabra oculta, las letras incorrectas y el dibujo progresivo del ahorcado.
Al finalizar (ganar o perder), el usuario puede:
Presionar ENTER para iniciar una nueva partida.
Presionar ESC para regresar al menú o salir.
2. Librerías utilizadas
El proyecto utiliza las siguientes librerías:
• Pygame
Usada para la creación de la ventana, captura de eventos del teclado, renderizado de texto, dibujo del ahorcado y animaciones de la barra de carga.
Instalación:
pip install pygame
4. Detalles relevantes sobre el funcionamiento
5. El dibujo del ahorcado se divide en seis etapas, correspondientes a los errores cometidos por el usuario.
El juego selecciona una palabra aleatoria de una lista interna predefinida.
Se utilizan funciones independientes para mantener una estructura modular:
Menú principal
Pantalla de carga
Lógica del juego
Sistema de dibujo del personaje
