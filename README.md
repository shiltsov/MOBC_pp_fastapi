# MOBC_pp_fastapi
Итоговый проект по курсу "прикладной python"

## Задание 
Реализовать какой-нибудь сервис с использованием фреймворка Fasapi желательно связанный к курсовой работой и ML

## Дисклеймер
В рамках курсовой работы у нас там все уже реализовано (не мной), а хотелось самому отдельно тоже попрактиковаться, поэтому делаю отдельно.
Реализовал на усмотрение 7 ручек (из требуемых 5, но содержательных получилось 6)

проект доступен по адресу: http://35.188.77.163:8000

### Что задействовано в проекте
- база данных `Postgresql` в связке с ORM `SqlAlchemy` (хотел задействовать `Alembic` но не нашел к чему его тут применить. Тем не менее немного поэкспериментировал с ним отдельно)
- кеширование `Redis` (в режиме демонстрации того что я умею это настраивать и использовать)
- схемы данных `Pydentic`
- разворачивание проекта с помощию `dokcer-compose` из 3-х составных частей - 2  готовых образов (Postgres и Redis) + 1 своего (Fastapi)

### С чем не справился:
для логирования мне нужны внешние IP адреса внутри контейнера, заголовки "в лоб" не пробрасываются, какие-то несложные решения 
в стиле извлечения данных их хедеров результата не дали, пробовал делать черед middleware - не взлетело. Возможно дело в том что 
использую uvicorn - пробовал слегка gunicorn котоый рекомендовался в лекциях, но тяпляпить не люблю, а на серьезное вникание в этот 
вопрос времени уже не остается. Так или иначе это не must-have, надеюсь на оценку это не повлияет (для извлечения IP вззде в коде
использую request.client.host). 

### Что сделано
Проект состоит из двух зон - админской (префикс /admin/ и раутер admin.py) и общий (без префикса, раутер common.py)
реализованы ручки

общедоступные ручки
- `GET /` - выдает приветственоное сообщение на испанском языке
- `POST /predict` требует отправки текстового файла (file) возвращает предикт (id автора, имя автора, уверенность модели в ответе)
- `POST /vote` - требует начение vote (от 1 до 5) возвращает ответ что проголосовали либо выбрасывает ошибку если неверное число
- `GET /stat` - возвращает статистику голосований (число голосовавших и средний рейтинг)

следующие ручки требуют токена (Bearar Token `Token` `eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81` - задается в .env)
- `POST /admin/votelog` - выгрузка рейтинга (возвращает csv файл)
- `POST /admin/predictlog` - выгрузка текстов из отправляемых пользователями файлов (возвращает csv файл)
- `GET /admin/stat` - информация об операционной системе (загрузка CPU и тд). Единственное место куда можно прицепить кеширование - именно сюда я его и прицепил 

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/e024d9cc-4c7c-4148-8b74-b73c90b4b7e7)

## Пояснение по структуре проекта

app - приложение<br>
   models - выгруженные модели
   routers - раутеры<br>
      common.py - общие<br>
      admin.py - требующие авторизации <br>
   schemas.py - схемы данных<br>
   database.py - интерфейс с базой<br>
   models.py - ORM (таблицы)<br>
   main.py - старт<br>
   ml.py - все что связано с ML<br>

initdb - папка куда помещаем SQL для начальной загрузки базы (сделано отдельно через SqlAlchimi - файл create_sql.py) докер оттуда автоматически все загрузит при старте

## Инструкция по развертыванию

скачиваем, создаем .env файл в папке add (параметры ниже) делаем `$ docker-compose up`, если заработало - то все хорошо

POSTGRES_HOST=db<br>
POSTGRES_USER=user<br>
POSTGRES_PASSWORD=pass<br>
POSTGRES_DB=db<br>
ADMIN_TOKEN=eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81<br>

