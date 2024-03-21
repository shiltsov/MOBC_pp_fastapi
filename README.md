# MOBC_pp_fastapi
Итоговый проект по курсу "прикладной python"

ВШЭ МОВС-23 Шильцов Дмитрий (sda@asperito.ru @DDmmiittrryy)

## Задание 
Реализовать какой-нибудь сервис с использованием фреймворка Fasapi желательно связанный к курсовой работой и ML

## Дисклеймер
В рамках курсовой работы у нас там все уже реализовано (не мной), а хотелось самому отдельно тоже попрактиковаться, поэтому делаю отдельно.
Реализовал суммарно 7 ручек (из требуемых 5, но содержательных получилось 6)

проект доступен по адресу: http://35.188.77.163:8000

### Что задействовано в проекте
- база данных `Postgresql` в связке с ORM `SqlAlchemy` (хотел задействовать `Alembic` но не нашел к чему его тут применить. Тем не менее немного поэкспериментировал с ним отдельно)
- кеширование `Redis` (в режиме демонстрации того что я умею это настраивать и использовать)
- схемы данных `Pydentic`
- разворачивание проекта с помощию `dokcer-compose` из 3-х составных частей - 2  готовых образов (Postgres и Redis) + 1 своего (Fastapi)

### Что сделано
Проект состоит из двух зон - админской (префикс /admin/ и раутер admin.py) и общий (без префикса, раутер common.py)
реализованы ручки

общедоступные ручки
- `GET /` - выдает приветственное сообщение на испанском языке
- `POST /predict` требует отправки текстового файла (file) возвращает предикт (id автора, имя автора, уверенность модели в ответе)
- `POST /vote` - требует начение vote (от 1 до 5) возвращает ответ что проголосовали либо выбрасывает ошибку если неверное число
- `GET /stat` - возвращает статистику голосований (число голосовавших и средний рейтинг)

следующие ручки требуют токена (Bearar Token `Token` `eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81` - задается в .env)
- `POST /admin/votelog` - выгрузка рейтинга (возвращает csv файл)
- `POST /admin/predictlog` - выгрузка текстов из отправляемых пользователями файлов (возвращает csv файл)
- `GET /admin/stat` - информация об операционной системе (загрузка CPU и тд). Сюда я прицепил кеширование. Проверил  - работает :)

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/3d13c676-87d8-4b82-b0da-06884764a2fa)


## Пояснение по структуре проекта

`app` - приложение<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`models` - выгруженные модели<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`routers` - раутеры<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`common.py` - общие<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`admin.py` - требующие авторизации <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`schemas.py` - схемы данных<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`database.py` - интерфейс с базой<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`models.py` - ORM (таблицы)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`main.py` - старт<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ml.py` - все что связано с ML<br>

`initdb` - папка куда помещаем SQL для начальной загрузки базы, докер оттуда автоматически все загрузит при старте

в корне также лежат 3 текстовых файла `test-pushkin.txt` `test-simple.txt` `test-turgenev.txt` - чтобы не искать чем тестить

## Инструкция по развертыванию

скачиваем, создаем .env файл в папке app (параметры ниже) делаем `$ docker-compose up`, если заработало - то все хорошо

POSTGRES_HOST=db<br>
POSTGRES_USER=user<br>
POSTGRES_PASSWORD=pass<br>
POSTGRES_DB=db<br>
ADMIN_TOKEN=eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81<br>

### Лог развертывания на сервере

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/539fa820-8ed8-4d10-81ce-65ffd3ec103a)

### Скрины из Postman 

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/eb554fee-8f81-44a2-81d8-4df2e54e84d9)

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/c9ba5db3-d0aa-4ecb-bf3c-6fdade6d76a1)

![изображение](https://github.com/shiltsov/MOBC_pp_fastapi/assets/54742337/dcab9f92-6f95-4da9-b73a-76a5bf9c4579)


