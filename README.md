# Yalantis_2021


После скачивания репозитория в отдельную папку с помощью стандаhтных инструментов Git и перехода в корневую папку проекта :

        git pull https://github.com/Pirognoe/Yalantis_2021.git

необходимо установить все зависимости для проекта с помощью менеджера пакетов (если Вы пользователь Windows можно просто набрать `cmd` в проводнике для начала):

        pip install -r requirements.txt

После успешной установки из корневого каталога запускаем наш **_Django_** проект с помощью стандартных команд [Docs] (https://docs.djangoproject.com/en/3.2/) :

        python manage.py runserver

Запустится локальный сервер ( по умолчанию на Windows это http://127.0.0.1:8000/ ) и перейдя на `http://127.0.0.1:8000/courses` увидим приятный UI интерфейс для нашего API в браузере

 ![Main_API_list](https://user-images.githubusercontent.com/17066017/117063046-ec539900-ad2c-11eb-8ae0-2b3556ac67d2.PNG)
 
 При нажатии на кнопку Filters можно осуществить поиск по названию и фильтр по датам начала и окончания курсов
 ![Filter_screen](https://user-images.githubusercontent.com/17066017/117063612-bc58c580-ad2d-11eb-8b39-e33b31c44160.PNG)

Для редактирования какой-то конкретной записи достаточно перейти на кокретный ендпоинт, например `http://127.0.0.1:8000/courses/2/`
