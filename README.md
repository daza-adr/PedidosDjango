# PedidoFácil

Aplicación web de gestión de productos y pedidos desarrollada con Django.

## Requisitos

- Python 3.12+
- Django 6.1
- PostgreSQL (opcional para producción con Neon)

## Instalación local

1. Clona el repositorio.
2. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:

   ```bash
   copy .env.example .env
   ```

   Define `DATABASE_URL` en `.env` para conectar PostgreSQL/Neon. Si no defines una URL, la aplicación usará SQLite local.

5. Aplica migraciones:

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

7. Ejecuta la aplicación:

   ```bash
   python manage.py runserver
   ```

8. Ingresa en `http://127.0.0.1:8000` y usa el login con tu usuario.

## Funcionalidades implementadas

- Inicio y cierre de sesión con Django Authentication.
- CRUD de productos.
- CRUD de pedidos.
- Validaciones con JavaScript en formularios del cliente.
- Validaciones en Django en el servidor.
- Búsqueda por nombre de producto o cliente.
- Restricción de acceso a usuarios autenticados.
- Interfaz bootstrap responsive.

## Variables de entorno

La aplicación usa `DATABASE_URL` para la conexión recomendada a PostgreSQL/Neon. También admite la configuración por campos separados:

- `DATABASE_URL`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `SECRET_KEY`
- `DEBUG`

Cuando no se envían variables de PostgreSQL, el proyecto se ejecuta con SQLite.

## Despliegue en Render

1. Crea un proyecto en Render.
2. Conecta el repositorio de GitHub.
3. Configura la web service con el comando:

   ```bash
   python manage.py migrate && python manage.py collectstatic --noinput
   ```

4. Define `DATABASE_URL` con la cadena de conexión de Neon y configura `SECRET_KEY` y `DEBUG` como variables de entorno.
5. Publica la aplicación.

## Seguridad

- Las contraseñas se gestionan con el sistema de autenticación de Django.
- No se almacenan contraseñas en texto plano.
- Los usuarios no autenticados son redirigidos al login.
