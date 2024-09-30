# Primeros pasos

Django es un framework ORM; básicamente, crearemos clases (modelos) que se migrarán como entidades de base de datos (SQL), independientemente del sistema de base de datos utilizado para el proyecto.

## Crear tu proyecto de Django

    django-admin startproject <nombre_del_proyecto>

## Integrando Migraciones

Si te preguntas por qué hacemos esto, es porque Django viene por defecto con ciertas configuraciones ya establecidas, como módulos de administración, autenticación, etc.

    python manage.py migrate

Antes de que ejecutes este comando, ten en cuenta que se creará una base de datos por defecto en SQLite, ya que así está configurado. Sin embargo, esto se puede modificar en el archivo settings.py, en la sección DATABASES, lo que te permitirá usar otra base de datos (Oracle, PostgreSQL, etc.).

Aquí tienes un ejemplo para MySQL:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombreDB',
            'USER': 'nombreusuario',
            'PASSWORD': 'pass',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

## Ejecutar el servidor de Django

    python manage.py runserver

![iniciando_servidor](https://github.com/user-attachments/assets/9031cd9c-c4a1-456e-a7df-c3b58820d629)
