# 📊 Статистика + Админка

Проект состоит из двух независимых частей:  
- **Frontend** — Vue 3 приложение с маршрутизацией (Vite + Vue Router)  
- **Backend** — Django REST API для хранения и обновления данных  

На главной странице отображается динамическая статистика. Через админ-панель можно изменить значения, и они сразу отразятся на главной.

---

## 🗂 Структура проекта
```
project-root/
├── frontend/ # Vue 3 приложение
│ ├── src/
│ │ ├── views/
│ │ │ ├── HomeView.vue # Главная страница со статистикой
│ │ │ └── AdminView.vue # Админка для редактирования
│ │ └── ...
│ └── ...
│
├── backend/ # Django-проект
│ ├── api/ # Django-приложение с API
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── serializers.py
│ │ └── ...
│ └── backend/ # Настройки проекта (settings.py, urls.py и т.д.)
│
└── README.md
```
---

## 🚀 Запуск проекта
### 1. Запуск бэкенда **Django**
+ Перейдите в папку *backend*:
<code>cd backend</code>

+ Установите зависимости:

`pip install django djangorestframework django-cors-headers`

+ Примените миграции:

`python manage.py migrate`

+ Запустите сервер:

`python manage.py runserver`

✅ API будет доступно по адресу: `http://127.0.0.1:8000/api/data/` 

### 2. Запуск фронтенда (Vue 3)
+ Откройте новый терминал и перейдите в папку frontend:

`cd frontend`
+ Установите зависимости:

`npm install`

+ Запустите dev-сервер:

`npm run dev`

✅ Приложение будет доступно по адресу: `http://localhost:5173`
## 🌐 Страницы
|Endpoint|Описание|
|:-|:-|
|`/`|**Главная** — отображает статистику: `position`,`percent`,`year`,`days`|
|`/admin`|**Админка** — форма для редактирования этих значений| 
## 🛠 Технологии
#### Frontend: `Vue 3`, `Vue Router`, `Vite`, `JavaScript`, `fetch`

#### Backend: `Python 3.13+`, `Django 5.2`, `Django REST Framework`

#### API: `REST`, `JSON`

#### Связка: `HTTP-запросы из Vue к Django`
