### Курсовая работа 5. Работа с Базой Данных.

# Программа по поиску работодателей на hh.ru. Сохранение их вакансий в БД PostgreSQL и запросы по выводу информации с БД

## Основные шаги проекта:

# Получены данные о работодателях и их открытых вакансиях с сайта hh.ru. Для этого был использован публичный API hh.ru и библиотека requests.
# Спроектированны таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД использовалась библиотека psycopg2.
# Создан класс DBManager для работы с данными в БД

## Установка и запуск:

# Склонируйте репозиторий с проектом: git clone <URL_репозитория>
# Установите необходимые зависимости: pip install -r requirements.txt
# Создать файл с названием database.ini, который заполняется следующим образом: [postgresql] host=YourHost database=YourDatabase user=YourUser password=YourPassword
# Запустите программу: python main.py

## Использование
# При запуске программы вы увидите список доступных действий. Введите свои данные для подключения к базе данных, затем выберите действие, введя соответствующую цифру. 

## Программа предоставляет следующие возможности:
# Получать список всех компаний и количество вакансий у каждой компании.
# Получать список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
# Просмотр средней зарплаты.
# Получать среднюю зарплату по вакансиям.
# Список всех вакансий, у которых зарплата выше средней по всем вакансиям.