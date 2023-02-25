# Proyecto final

Este proyecto es sobre un blog orientado a D&D, donde se puede realizar un CRUD tanto de armas como de hechizos. La idea es que los usuarios puedan subir tanto contenido original de D&D como Homebrew, ya que también existe la posibilidad de dejar una opinión sobre los hechizos subidos (funcion aún no disponible para las armas).

Para dejar un comentario sobre un hechizo, es necesario primero estar registrado y logueado en la página. Una vez hecho esto, debemos ir a la parte de "Hechizos" donde se podrá visualizar en forma de lista todos los hechizos guardados en la base de datos. Además de los botones de detalles, editar y borrar, encontraremos el de "opinar"

Una vez enviada la opinión, podremos buscarla en en inicio. La búsqueda se realiza por nombre de hechizo.


- comandos:

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver 

