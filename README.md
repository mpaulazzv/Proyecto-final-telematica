# Proyecto-final-telematica
**Estudiante:**
María Paula Flórez Varags

Repositorio que contiene el proyecto final de telemática. Consiste en la estructura de una red social basada en contenedores.

**Descripción:**

La aplicación principal es app1.py, la cual está desarrollada sobre Python.

Simula la creación y el inicio de sesión de los usuarios de una red social. Cuando se crea un usuario, se escribe su información en una base de datos (base_datos.csv) y se le asiga el puerto sobre el cual se construirá su contenedor. Al crear el usuario, se construye su contenedor utilizando un archivo Dockerfile, y sobre este contenedor se ejecutará la aplicación de usuario (app2.py).

Para correr el contenedor creado, debe iniciar sesión ingresando las credenciales con las que creó el usuario. En caso tal de que el usuario esté registrado, entonces se pondrá a correr una imagen con su nombre que toma como base el contenedor construido previamente y será redirigido automáticamente a su página personal.


**Requisitos:**

- Tener docker
- Tener a docker como usuario sudoer 
- Tener python3.10
- Tener las librerías FLask y Pandas de Python instaladas
- Tener los puertos 80 y del 8000 en adelante desocupados

En caso de no tener ninguna, ejecutar los siguientes comandos en su terminal:

- sudo apt update
- sudo apt install docker-compose
- sudo apt install python3.10 -y
- sudo apt install python3-pip -y
- sudo pip3.10 install flask
- sudo pip3.10 install Pandas

Para poner a docker como usuario sudoer, ejecutar el siguiente comando y luego reiniciar su máquina:

sudo usermod -aG docker $USER

**Instrucciones:**

1. Descargar el .Zip o ejecutar en su terminal: git clone https://github.com/mpaulazzv/Proyecto-final-telematica
2. Ubicarse en la carpeta raíz del proyecto y ejecutar: sudo python3.10 app1.py
3. Digitar en el buscador de su navegador: "localhost:80", que lo dirigirá a la url principal de la red social
4. Para crear un usuario dirigirse a localhost/crear_usuario
5. Ingresar un nombre de usuario y una contraseña
6. Ejecutar "cat base_datos.csv" para validar que se haya escrito correctamente la base de datos y verificar el puerto que le corresponde
7. Para acceder a su página de usuario debe dirigirse a localhost/login para iniciar sesión
8. Ingresar los datos que utilizó al crear el usuario y será redirigido automáticamente a su paǵina de usuario (que es un contenedor) con su respectivo puerto, en caso de que parezca que no carga la página, simplemente refrésquela
9. Para verificar los contenedores que están corriendo en su máquina, ejecutar: "docker ps"

