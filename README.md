# Proyecto-final-telematica
Repositorio que contiene el proyecto final de telemática. Consiste en la estructura de una red social basada en contenedores.

**Descripción:**

La aplicación principal es app1.py, la cual está desarrollada sobre Python.

Simula la creación y el inicio de sesión de los usuarios de una red social. Cuando se crea un usuario, se escribe su información en una base de datos (base_datos.csv) y se le asiga el puerto sobre el cual se construirá su contenedor. Al crear el usuario, se construye su contenedor utilizando un archivo Dockerfile, y sobre este contenedor se ejecutará la aplicación de usuario (app2.py).

Para correr el contenedor creado, debe iniciar sesión ingresando las credenciales con las que creó el usuario. En caso tal de que el usuario esté registrado, entonces se pondrá a correr una imagen con su nombre que toma como base el contenedor construido previamente y será redirigido automáticamente a su página personal.

**Requisitos:**

- Tener docker
- Tener python3.10
- Tener las librerías FLask y Pandas de Python instaladas

En caso de no tener ninguna, ejecutar los siguientes comandos en su terminal:

- sudo apt update
- sudo apt install docker-compose
- sudo apt install python3.10 -y
- sudo apt install python3-pip -y
- sudo apt pip3.10 install flask
- sudo apt pip3.10 install Pandas

**Instrucciones:**

1. Ubicarse en la carpeta raíz del proyecto y ejecutar: sudo python3.10 app1.py
2. Digitar en el buscador de su navegador: localhost, que lo dirigirá a la url principal de la red social
3. Para crear un usuario dirigirse a localhost/crear_usuario
4. Ingresar un nombre de usuario y una contraseña
5. Para acceder a su página de usuario debe dirigirse a localhost/login
6. Ingresar los datos que utilizó al crear el usuario y será redirigido automáticamente a su paǵina de usuario (que es un contenedor) con su respectivo puerto, en caso de que parezca que no carga la página, simplemente refrésquela

