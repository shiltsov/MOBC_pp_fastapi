FROM python:3.11-slim
LABEL maintainer="sda@asperito.ru"

# Создаем каталог /app внутри контейнера

# Копируем requirements.txt в /app
RUN mkdir /fastapi_app
WORKDIR /fastapi_app

COPY ./requirements.txt /fastapi_app/requirements.txt
RUN pip install wheel setuptools pip --upgrade && pip install --no-cache-dir --upgrade -r /fastapi_app/requirements.txt


COPY . /fastapi_app/app
EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

