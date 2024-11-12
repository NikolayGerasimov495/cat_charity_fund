# QRKot - Благотворительный фонд поддержки котиков

## Стек 
    Python FastAPI SQLAlchemy Pydantic Flake8


## Описание проекта

QRKot - это приложение для Благотворительного фонда поддержки котиков, которое собирает пожертвования на различные целевые проекты, такие как медицинское обслуживание, обустройство кошачьих колоний и помощь бездомным кошкам. 

## Функционал

### Проекты
- Возможность создания нескольких целевых проектов.
- Каждый проект имеет название, описание и сумму, которую необходимо собрать.
- Проекты закрываются после достижения необходимой суммы.

### Пожертвования
- Пользователи могут делать пожертвования с комментариями.
- Пожертвования распределяются по принципу First In, First Out (FIFO).
- Если пожертвование превышает необходимую сумму, оставшиеся средства ждут открытия следующего проекта.

### Пользователи
- Администраторы могут создавать и управлять проектами.
- Все пользователи могут просматривать список всех проектов и своих пожертвований.

## Предварительная настройка

1. Клонируйте репозиторий с тестами для Вашего финального проекта:
   ```bash
   git clone git@github.com:NikolayGerasimov495/cat_charity_fund.git
   cd cat_charity_fund
2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
    
3. Установите необходимые пакеты:

    ```bash
    pip install -r requirements.txt
   
4. Создайте приложение на FastAPI в директории app/.

## Технические подробности:

### Модели

Пользователи: Используйте библиотеку FastAPI Users для управления пользователями.
Проекты: Модель CharityProject с полями:

    - id
    - name
    - description
    - full_amount
    - invested_amount
    - fully_invested
    - create_date
    - close_date
Пожертвования: Модель Donation с полями:

    - id
    - user_id
    - comment
    - full_amount
    - invested_amount
    - fully_invested
    - create_date
    - close_date

## API
Спецификация API доступна в файле openapi.json. Для просмотра документации загрузите файл на сайт ReDoc.

## Настройки базы данных

Подключение к базе данных по умолчанию: sqlite+aiosqlite:///./fastapi.db.

## Запуск приложения

### Для запуска приложения используйте команды:

    uvicorn app.main:app --reload
    alembic init --template async alembic
    alembic revision --autogenerate -m "migration name"
    alembic upgrade head
    alembic downgrade
    pytest

# Автор 
##### **Николай Герасимов**