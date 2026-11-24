# 🌱 Tierra Viva — Página informativa sobre la composta

## 🎯 Objetivo
Tener:
* Proyecto Django funcionando
* App `composta` con páginas informativas
* Plantillas con herencia (`base.html`) y Tailwind CSS
* Fotos reales (Wikimedia Commons) en archivos estáticos

## 1 Crear entorno virtual y proyecto
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
django-admin startproject config .
python manage.py startapp composta
```

## 2 Configurar settings.py
📌 Agregar app
```python
INSTALLED_APPS = [
    ...
    'composta',
]
```
📌 Idioma
```python
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
```

## 3 URLs
📁 config/urls.py
```python
path('', include('composta.urls')),
```

| Ruta | Vista | Página |
|---|---|---|
| `/` | `home` | ¿Qué es una composta? |
| `/como-hacerla/` | `como_hacer` | Paso a paso |
| `/materiales/` | `materiales` | Qué sí y qué no |
| `/beneficios/` | `beneficios` | Beneficios y usos |
| `/preguntas/` | `preguntas` | Preguntas frecuentes |
| `/creditos/` | `creditos` | Créditos de las fotos |

## 4 Vistas
Cada vista arma listas de diccionarios (pasos, materiales, preguntas…) y las manda
a la plantilla con `render()`. La plantilla las recorre con `{% for %}`.

## 5 Plantillas y estáticos
```
composta/
├── templates/composta/
│   ├── base.html              ← navbar, footer, Tailwind
│   ├── partials/page_hero.html← portada reutilizable ({% include %})
│   ├── home.html
│   ├── como_hacer.html
│   ├── materiales.html
│   ├── beneficios.html
│   ├── preguntas.html
│   └── creditos.html
└── static/composta/img/       ← fotos
```

## 6 Correr el proyecto
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Abrir http://127.0.0.1:8000/
