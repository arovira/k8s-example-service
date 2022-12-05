FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install poetry==1.2.2

COPY src/ /app
WORKDIR /app

RUN poetry install

CMD poetry run uvicorn --host=0.0.0.0 app.main:app
