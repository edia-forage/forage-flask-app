FROM python:alpine3.7

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r /app/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ADD . /app
ENV PORT 8080

CMD ["gunicorn", "app:app", "--config=config.py"]
