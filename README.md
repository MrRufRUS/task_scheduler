# Task Scheduler

Асинхронный планировщик задач на Python с использованием FastAPI, SQLAlchemy и SQLite.

## Требования

- Python 3.12+
- Poetry (для управления зависимостями)

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/MrRufRUS/task_scheduler
cd task_scheduler
```

### 2. Установите зависимости

```bash
poetry install
```

### 3. Активируйте виртуальное окружение

```bash
. .venv/Scripts/activate
```
## Cоздайте начальную миграцию БД

```bash
# Удалите старую БД если нужно
rm ./db.sqlite3

# Создадим папку versions
cd alembic
mkdir versions

# Сгенерируйте миграцию
alembic revision --autogenerate -m "initial"

# Примените миграции
alembic upgrade head
```

## Запуск приложения

```bash
python main.py
```

Приложение запустится на `http://localhost:8000`.

### API документация

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Структура проекта

```                                                                                            
├── README.md                                          # Инструкция запуска
├── alembic                                            
│   ├── README                  
│   ├── env.py                                         
│   ├── script.py.mako                                 # Шаблоны миграции
│   └── versions/                                      # Миграции
├── alembic.ini                                        # Конфигурация Alembic
├── app                                                # Каталог Веб-приложения
│   ├── __init__.py 
│   ├── api                                            
│   │   ├── __init__.py
│   │   ├── crud                                       # CRUD операции
│   │   │   ├── __init__.py
│   │   │   └── tasks.py
│   │   ├── endpoints                                  # Ручки (эндпоины)
│   │   │   ├── __init__.py
│   │   │   └── tasks.py
│   │   └── schemas                                    # Pydantic схемы
│   │       ├── __init__.py
│   │       └── tasks.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py                                  # Конфигурация приложения
│   └── db
│       ├── __init__.py
│       ├── database.py                                # Подключение к БД
│       └── models.py                                  # Модели данных SQLAlchemy
├── db.sqlite3                                         # БД SQLite3
├── main.py                                            # Главный исполняемый файл
├── poetry.lock                                   
├── poetry.toml                                        # Конфиг Poetry
├── pyproject.toml                                     # Зависимости проекта
└── worker                                             # Worker для обработки задач
    ├── __init__.py                                    
    └── worker.py

```

## Модели

### Task

Таблица для хранения задач:

| Поле | Тип | Описание |
|------|-----|---------|
| `id` | Integer | Первичный ключ |
| `create_time` | DateTime | Время создания задачи |
| `start_time` | DateTime | Время начала выполнения |
| `time_to_execute` | Float | Время выполнения в секундах |

## Разработка

### Создание новой миграции

```bash
alembic revision --autogenerate -m "description"
```

### Применение миграций

```bash
alembic upgrade head
```

### Откат последней миграции

```bash
alembic downgrade -1
```
