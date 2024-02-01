FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/online-shop

COPY requirements.txt /usr/src/requirements.txt

# Устанавливаем зависимости без использования sudo
RUN pip install --no-cache-dir -r /usr/src/requirements.txt && \
    rm -rf /root/.cache

COPY . /usr/src/online-shop

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
