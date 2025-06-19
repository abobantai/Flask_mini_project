# README

## Flask User Management System

Простой проект на Flask с регистрацией, логином, профилем пользователя и изменением профиля. Проект создан как демонстрация базовых навыков работы с Flask, SQLAlchemy, сессиями, хэшированием паролей и обработкой ошибок.

## Функционал

- Регистрация пользователя
- Хэширование пароля (безопасное хранение)
- Авторизация пользователя
- Сессии (хранение пользователя в сессии)
- Профиль пользователя (с отображением username, email, bio)
- Редактирование профиля
- Загрузка аватаров
- Разделение логики по Blueprints
- Обработка ошибок

## Технологии

- Python 3.12+
- Flask
- Flask-SQLAlchemy
- SQLite (локальная БД)
- Werkzeug (хэширование паролей)

## Установка

### 1. Клонирование проекта

```bash
git clone https://github.com/username/projectname.git
cd projectname
```

### 2. Создание виртуального окружения (рекомендуется)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Инициализация базы данных

```bash
python create_db.py
```

### 5. Запуск проекта

```bash
python run.py
```

## Структура проекта

```bash
projectname/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes/
│       ├── auth.py
│       ├── profile.py
│       └── settings.py
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── profile.html
│   └── change.html
│
├── static/uploads/  # Загруженные аватары
│
├── run.py
├── create_db.py
└── requirements.txt
```

## Примечание

- Пароли хранятся в хэшированном виде с использованием `werkzeug.security`.
- Blueprints позволяют разбивать проект на модули.
- Все настройки приложения задаются в `app/__init__.py`.

## Возможности для улучшения

- Добавить email-подтверждение регистрации
- Добавить JWT/REST API
- Реализовать загрузку и хранение аватаров через облако
- Docker-контейнеризация

---

Проект полностью написан вручную с целью обучения, в том числе с симуляцией реального небольшого веб-приложения.

