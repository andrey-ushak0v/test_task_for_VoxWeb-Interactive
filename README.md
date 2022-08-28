## Тестовое задание на позицию python-разработчик в VoxWeb Interactive

проект парсит 10 последних новостей с Яндекс.маркет и заносит их в базу данных MYsql
кастомизированна админка, с помощью adminLTE3

#запуск

1)склонируйте репозиторий на свой компьютер:

2)создайте и установите виртуальное окружение:

```python3 -m venv venv```

```source venv/bin/activate```

3)установите в виртуальное окружение зависимости из файла requirerments.txt:

```pip install -r requirements.txt```

4)установите на свой компьютер MYsql и mysqlclient:

5)в настройках проекта установите настройки базы данных:


```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```


6)из директории с файлом manage.py создайте и накатите миграции: 

```python3 manage.py makemigrations```

```python3 manage.py migrate```

7)выполните файл parser.py

8)из директории с файлом manage.py выполните команду:

```python3 manage.py load_data_to_db```

9)создайте суперпользователя для входа в админку:

```python3 manage.py createsuperuser```

10)запустите локальный сервер:

```python3 manage.py runserver```

11)в браузере перейдите по адресу:

``` http://127.0.0.1:8000/admin/ ```




