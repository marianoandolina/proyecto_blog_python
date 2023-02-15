![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

# ¡Proyecto Blog! [Python]
Este repositorio contiene todos los materiales e instrucciones para poder realizar el proyecto de blog de programador python.

Este proyecto se acerca al tipo de trabajo y de desafios que tendrán en el curso de Python Django.

Para este proyecto ya cuenta con toda la parte de frontend resuelta, su deber será crear el backend de esta aplicación.

__NOTA__: Recomendamos haber realizado todos los ejercicios de pŕactica para poder realizar este proyecto, principalmente los de:
- SQLAlchemy ORM
- APIs y WebApp

## Objetivo
El objetivo es construir el backend de una aplicación de blog. El frontend ya se encarga del login del usuario y mostrar la información que provee el backend (enviar información y consultar al backend). El backend deberá:
- Proveer los endpoints que muestren las páginas HTML.
- Proveer los endpoints para la generación de posteos en el blog como también consultar los posteos realizados de un usuario.

Para lograr esto, además de crear todos los endpoints necesarios deberá crear la base de datos para almacenar toda la información (posteos) que la aplicación vaya generando.

## Recursos
- Contará con todos los archivos necesarios de frontend en las carpeta templates y static.

## Como comenzar
- Deberá crear un archivo "app.py" en el cual colocará todo el código necesario para realizar el backend del proyecto.
- Luego deberá crear el bloque principal `if __name__ == "__main__":`. Dentro del bloque principal deberá llamar al server:
```python
app.run(host="127.0.0.1", port=5000)
```
- Deberá incluir el llamado al decorador encargado de crear la clase ni bien ingresamos por primera vez a la página:
```python
# Este método se ejecutará solo una vez
# la primera vez que ingresemos a un endpoint
@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos
    db.create_all()
    print("Base de datos generada")
```

## Base de datos
Deberá crear la base de datos SQLite "blog.db". Utilizar SQLAlchemy para crear una clase que responda a la tabla "post". Dicha tabla "post" debe contener las siguientes columnas:
- id --> número (Integer) (autoincremental, primary_key)
- username --> texto (String) (nombre del usuario que hizo el post)
- titulo --> texto (String) (título del post)
- texto --> texto (String) (texto/contenido del post)


## Endpoints del frontend (HTML) # COMPLETADO #
Dentro del archivo __app.py__ deberá implementar los siguientes endpoints que responderan a las rutas del explorador del usuario.

### Endpoint login (/login) # COMPLETADO #
Cuando el usuario acceda a esta ruta desde el explorador, este endpoint deberá renderizar (render_template) el archivo html "login.html"

### Endpoint de bienvenida o index (/) # COMPLETADO #
Cuando el usuario acceda a esta ruta desde el explorador, este endpoint deberá renderizar (render_template) el archivo html "blog.html"


## Endpoints del backend (APIs) # COMPLETADO #
Dentro del archivo __app.py__ deberá implementar los siguientes endpoints que responderán las peticiones GET / POST / etc:

### Endpoint post (/post) # COMPLETADO #
Dentro de este endpoint deberá aceptar peticiones del tipo "GET" y del tipo "POST". Para cada petición deberá realizar:

### Endpoint post (/post) para peticiones GET
Cuando este endpoint sea invocado por GET, el frontend le enviará por parámetros de la URL el username del usuario logeado en "request.args".
- Deberá obtener el username de "request.args". # COMPLETO
- Deberá filtrar los Posts por ese username y devolver los últimos (usar order_by descendente) tres posts realizados (limit = 3)
- Cada post lo deberá guardar en una lista de posts.
- Al finalizar deberá retornar los posts contenido en la lista como:
```python
return jsonify({"posts": posts}) 
```

### Endpoint post (/post) para peticiones POST
Cuando este endpoint sea invocado por POST, el frontend le enviará los datos del posteo escrito (username, titulo, texto) en los parámetros de un formulario en "request.form".
- Deberá obtener el username, titulo y texto de "request.form".
- Con esos datos deberá crear un nuevo posteo en la base de datos.
- Deberá almacenar el posteo creado en una variable llamada "post".
- Al finalizar deberá retornar que la petición se completó con éxito indicando los datos del posteo creado:
```python
return jsonify({"id": post.id, "titulo": post.titulo, "texto": post.texto})
```

## Puntos extra (bonus track)
En caso que desee mejorar el sistema puede implementar para el endpoint "/post" la petición DELETE.
- Cuando este endpoint sea invocado por DELETE, deberá borrar todo el contenido de la base de datos.