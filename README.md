🚀 Fullstack FastAPI + NGINX + PostgreSQL App
Это простой fullstack-проект, объединяющий:

FastAPI backend с подключением к PostgreSQL

NGINX frontend, обслуживающий статические файлы и проксирующий запросы к API

PostgreSQL в виде контейнера БД

Docker Compose для оркестрации всех сервисов

GitHub Actions для автоматического деплоя на продакшн-сервер

📁 Структура проекта
```
project-root/
├── .github/workflows/
│   └── main.yml                # CI/CD: GitHub Actions для деплоя
├── nginx/
│   ├── app.conf                # Конфигурация NGINX
│   ├── index.html              # Главная HTML-страница
│   ├── styles.css              # Стили
│   └── script.js               # JS-логика фронтенда
├── simple_python_app/
│   ├── app.py                  # FastAPI-приложение
│   ├── requirements.txt        # Зависимости Python
│   └── Dockerfile              # Dockerfile для backend-сервиса
├── docker-compose.yml          # Docker Compose для запуска всех контейнеров
├── .gitignore
└── README.md                   # Этот файл
```
⚙️ Быстрый старт (локально)
Требования:

Docker и Docker Compose

# Запуск проекта
docker compose up --build

После запуска:

Frontend доступен на: http://localhost:8049

Backend API: http://localhost:5000

Пример API-эндпоинта: http://localhost:5000/hello/World

🔁 CI/CD (GitHub Actions)
CI/CD настроен через .github/workflows/main.yml.
При каждом пуше в ветку main:

Запускается SSH-сессия на прод-сервер

Переходит в /compose

Выполняет git pull и docker-compose up -d --build

Для этого нужно настроить в GitHub репозитории:

PROD_SSH_PRIVATE_KEY – приватный SSH-ключ

PROD_SERVER_IP – IP-адрес прод-сервера

🧠 Что делает каждый компонент
nginx/app.conf
Обслуживает index.html, styles.css, script.js

Проксирует запросы на /api/ к FastAPI backend через simple_python_app:5000

simple_python_app/app.py
FastAPI-приложение с подключением к PostgreSQL через psycopg2

Эндпоинт / показывает версию PostgreSQL

Эндпоинт /hello/{name} возвращает приветствие

docker-compose.yml
Описывает 3 сервиса: web (nginx), simple_python_app (FastAPI), db (PostgreSQL)

Устанавливает сети и зависимости

depends_on и healthcheck обеспечивают порядок запуска

📦 Сборка и публикация образов (опционально)
Ты можешь модифицировать docker-compose.yml и GitHub Actions для пуша в Docker Hub.

📌 Примеры API

# Получение версии PostgreSQL
curl http://localhost:5000/

# Приветствие
curl http://localhost:5000/hello/Alex
