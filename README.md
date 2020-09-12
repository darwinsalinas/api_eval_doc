# API para la app de evaluación docente por parte del estudiante

Pasos para la correr el proyecto

- Clonar el repo

```bash
git clone git@github.com:darwinsalinas/api_eval_doc.git
```

- Instalar python3 si aun no lo tienes instalado

```bash
choco install -y python3
```

- Crear entorno virtual dentro de la carpeta del repo

```bash
python3 -m venv .envapievaldoc
```

- Activar entorno virtual en sistemas unix

```bash
source .envapievaldoc/bin/activate
```

- Activar entorno virtual en sistemas win

```bash
.envapievaldoc/Scrips/activate.bat
```

- Instalar dependencias

```bash
pip install -r requirements.txt
```

- Ejecutar servidor

```bash
python manage.py runserver
```


Si no quieres levantar el servicio en tu propia computadora puedes entrar a esta URL http://dsalinas.pythonanywhere.com/
