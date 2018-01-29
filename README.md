# Agora

The service portfolio management tool is a tool that allows a company / project to manage the portfolio of services they to maintain (offered to users / customers or internal).

### Dependencies

* [git](https://git-scm.com/)
* [virualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [pip](https://pypi.python.org/pypi/pip)

## Development instructions

### Get the code

```
git clone https://github.com/grnet/agora-sp.git
```

### Create a virtualenv for agora

```
cd agora
mkvirtualenv agora
```

### Install requirements

With virtualenv activated install dependencies

```
pip install -r requirements.txt
```

## Configuration

### Create configuration file

You can create a configuration file in order to override the default settings for the agora project. The default location of the .conf file is `/etc/agora/settings.conf`

The default contents of `settings.conf` are:

```
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.agora.sqlite3'
    }
}

DATABASES = SQLITE
EMAIL_FILE_PATH = '/tmp/agora/agora_emails'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
```

You should override it with your database settings, [you can read more information here](https://docs.djangoproject.com/en/1.9/ref/databases/).


### API configuration

As an extra step, you should also update the `resources/agora.spec` spec file,
and update the `root_url` attribute to reflect the url of the backend server.

Example: 

```
root_url: https://example.com
```


### Migrations

Run all migrations in order to construct the database schema.

You should run:

```
python manage.py migrate
```

Once migrations finish, you can run `python manage.py runserver` to test that the application is installed properly.


You can now view your application in `http://127.0.0.1:8000/`
