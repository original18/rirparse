# rirparse
Парсер магазина рыболовных товаров

Установка

1. Установите и настройте Python 3
2. Клонируйте репозиторий командой git@github.com:original18/rirparse.git
3. Из корневой директории проекта установите виртуальное окружение командой python -m venv venv
4. Установите зависимости командой pip install -r requirements.txt
5. Создайте файл .env с переменными:

    auth_url="http://riropt.ru/auth/"
    main_url="http://riropt.ru"
    url="https://riropt.ru/catalog/udilishcha/?PAGEN_1="
    login=Ваш_емеил
    password=Ваш_пароль

Запуск

Запустите файл writer.py