FROM python:3.11-alpine

WORKDIR '/app'

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./src .

EXPOSE 8000

CMD ["gunicorn", "renard.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
