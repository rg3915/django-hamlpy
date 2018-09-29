# django-hamlpy

Use HAML with Django and rendering Jinja2 example.

# Haml

[haml.info](http://haml.info/)

![haml01.png](myproject/core/static/img/haml01.png)

> Haml (HTML abstraction markup language)

É baseado em um princípio básico: marcação deve ser bonita.

```
*.haml
%section.container
  %h1= post.title
  %h2= post.subtitle
  .content
    = post.content
```

Estou usando [django-hamlpy](https://github.com/nyaruka/django-hamlpy) by [Nyaruka](https://github.com/nyaruka).


## Instalação

```
python3 -m venv .venv
source .venv/bin/activate
pip install django-hamlpy
```

Em `settings.py`, configure:

```python
TEMPLATES = [
    ...
    'APP_DIRS': False,
    'OPTIONS': {
        'loaders': (
            'hamlpy.template.loaders.HamlPyFilesystemLoader',
            'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
        ),
    ...
    },
]
```

E veja [index.haml](https://github.com/rg3915/django-hamlpy/blob/master/myproject/core/templates/index.haml)


## Para rodar este projeto

```
git clone https://github.com/rg3915/django-hamlpy.git
cd django-hamlpy
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
