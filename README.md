# Проект «API для Yatube»
## Спринт 9

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <ссылка>
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```