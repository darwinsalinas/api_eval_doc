# API para la app de evaluación docente por parte del estudiante

Pasos para la correr el proyecto

- Clonar el repo

```bash
git clone git@github.com:darwinsalinas/api_eval_doc.git
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
