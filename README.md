
PROYECTO: MENU DE RESTAURANTE - OLIVER AVILA
CURSO: COMPUTACION EN LA NUBE 
Esta aplicacion ha sido desarrollada en Python 3 utilizando  el framework Kivy. Su funcion es desplegar un menu de  restaurante interactivo que consume datos desde un archivoexterno en formato JSON.

REQUISITOS Utilizado :
- Python 3.x instalado.
- Libreria Kivy (Instalar con: pip install kivy).
- Archivo 'menu.json' presente en el mismo directorio.

INSTRUCCIONES DE EJECUCION:
1. Abrir la terminal o consola del sistema.
2. Navegar hasta la carpeta del proyecto.
3. Ejecutar el comando: python main.py

LOGICA DE NAVEGACION (SCREENMANAGER):
- Pantalla Inicio: Datos del desarrollador y boton de acceso.
- Pantalla Categorias: Carga automatica de secciones del JSON.
- Pantalla Productos: Listado de nombres y precios filtrados.

REGISTRO DE CAMBIOS (COMMITS):
En el repositorio de GitHub se han realizado 3 registros:
1. COMMIT_01: Creacion de main.py y definicion de pantallas.
2. COMMIT_02: Vinculacion con menu.json y carga de categorias.
3. COMMIT_03: Ajustes finales, validaciones y documentacion.

DEFINICION DE COMMIT:
Un commit es un registro o captura del estado del codigo en 
un punto especifico del tiempo. Permite documentar que fue
modificado y mantener un historial de versiones del proyecto.

COMANDO DE EJECUCION:
El ejecutable fue generado mediante PyInstaller con el comando:
pyinstaller --onefile --windowed main.py


DESARROLLADO POR: OLIVER CLAUDIO AVILA CASTILLO
