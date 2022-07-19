# Project «API for Yatube»

## Yandex Practicum. Python backend developer.

### About Yatube:
Yatube — is a social network. Пользователи пишут, читают и комментируют статьи. Users write, read and comment on articles. It is possible to subscribe to your favorite author. Mechanisms for registration, authentication, reset and password recovery are implemented.


### Description of the API project:
API Yatube создан для взаимодействия с основными функциями сервиса:

1. аутентификация пользователей — получение / создание / изменение / удаление публикаций
1. получение / создание / изменение / удаление комментариев
1. подписка на автора

#### Примеры запросов:
Получение списка постов:
```
GET http://127.0.0.1:8000/api/v1/posts/
content-type: application/json
```

Создание поста:
```
GET http://127.0.0.1:8000/api/v1/posts/
content-type: application/json
Authorization: Bearer <токен>
```

```
Получение JWT-токена:

POST http://127.0.0.1:8000/api/jwt/create/
content-type: application/json

{
    "username": "<логин>",
    "password": "<пароль>"
}
```
Подробный список всех запросов и примеры ответов в техническом задании (см. ниже)

### Техническое задание:
http://127.0.0.1:8000/redoc
* p.s. Ссылка активна только при запущенном сервере. Инструкция по запуску ниже.

### Используемые технологии::
* Django REST Framework
* Simple-JWT
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
Дмитрий Кирсанов
