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

    [Django server](C:\Users\Usuario\Desktop\python_backend\Proyectos_Djiango\img\iniciando_servidor.png)


## Creacion de una Aplicacion

Hemos creado nuestro proyecto, sin embargo, esto no es suficiente, necesitamos crear nuestras aplicaciones
que sera donde crearemos todo, en este caso, este proyecto sera dirigido para crear un Blog sencillo, con el siguiente comando crearemos nuestra aplicacion, con archivos por defecto de django....

Recuerda siempre estar en el directorio de tu proyecto para poder ejecutar el archivo **manage**

    python manage.py startapp <nombre_de_aplicacion>

## Agregar nuestra App al proyecto

Si bien creamos nuestra App, no significa que esta se ingresara de manera autonoma a la configuracion principal del proyecto, necesitamos ingresar nuestra app a la configuracion del sitio, accediendo al archivo **settings.py** del proyecto principal y en la seccion **INSTALLED_APPS = []** escribimos lo siguiente:

    '<modulo>.apps.<nmbre_del_modulo>Config'

El resultado seria algo como esto

    //orginal
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    //Modificado
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Blog.apps.BlogConfig'
    ]

Ya que hemos agregado nuestra app a la configuracion principal del sitio, tenemos que migrar esta informacion, para crear la entidad a la Base de datos, aplicamos el siguiente comando, con el archivo manage principal
    
    python manage.py makemigrations <App>

    python manage.py makemigrations Blog

salida de la consola:

    Migrations for 'Blog':
    Blog\migrations\0001_initial.py
        + Create model Post

Si quieres visualizar la tabla creada puedes usar el siguiente comando

    python manage.py sqlmigrate <app> <numero de la migracion>

resultado:

    BEGIN;
    --
    -- Create model Post
    --
    CREATE TABLE "Blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "update" datetime NOT NULL, "status" varchar(2) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);  
    CREATE INDEX "Blog_post_slug_e910c9eb" ON "Blog_post" ("slug");
    CREATE INDEX "Blog_post_author_id_89a23590" ON "Blog_post" ("author_id");
    CREATE INDEX "Blog_post_publish_3fcdce_idx" ON "Blog_post" ("publish" DESC);
    COMMIT;

Para continuar, Migra nuevamente la pagina 

    python manage.py migrate