# Электронная Торговая Сеть

## Описание Проекта

Этот проект представляет собой веб-приложение, предназначенное для управления иерархической структурой сети по продаже
электроники. В приложении реализованы функции для управления заводами, розничными сетями и индивидуальными
предпринимателями, а также отслеживания продуктов, предлагаемых этими компаниями. Основная цель проекта - обеспечить
эффективное управление и мониторинг взаимоотношений и операций внутри сети.

## Стек Технологий

- Python 3.11
- Django 3+
- Django REST Framework 3.10+
- PostgreSQL 10+
- Flake8 для линтинга
- Black для форматирования кода

## Инструкция по Запуску

Для запуска проекта выполните следующие шаги:

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/igorzinoviev08/TechTreeNetwork.git
   cd TechTreeNetwork
2. **Создание и активация виртуального окружения:**
    ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
3. **Установка зависимостей:**
    ```bash
   pip install -r requirements.txt
4. **Создайте файл .env в корневой директории проекта и добавьте в него переменные среды, например:**
   * SECRETKEY='КЛЮЧ DJNAGO ПРОЕКТА'
   * DOMAIN_NAME='АДРЕС ДОМЕНА'
   * POSTGRES_HOST='ХОСТ БД'
   * POSTGRES_DB='НАЗВАНИЕ БД'
   * POSTGRES_USER='ИМЯ ПОЛЬЗОВАТЕЛЯ БД'
   * POSTGRES_PASSWORD='ПАРОЛЬ ОТ БД'
5. **Настройка базы данных:**
   * Убедитесь, что у вас установлен PostgreSQL и он запущен.
   * Создайте базу данных для проекта через psql или pgAdmin.
   * Убедится что 4-й пункт выполнен (создан и заполнен файл .env)
6. **Применение миграций:**
   ```bash
   python manage.py migrate
7. **Запуск сервера:**
   ```bash
   python manage.py runserver

## Эндпоинты API
- GET /api/companies/ - получение списка всех компаний.
- POST /api/companies/ - создание новой компании.
- GET /api/companies/{id}/ - получение информации о конкретной компании.
- PUT /api/companies/{id}/ - обновление информации о компании.
- DELETE /api/companies/{id}/ - удаление компании.

## Автор проекта

Этот проект создан и поддерживается Зиновьевым Игорем.

Если у вас есть вопросы или предложения по улучшению проекта, свяжитесь со мной по адресу igor.zinoviev08@yandex.ru