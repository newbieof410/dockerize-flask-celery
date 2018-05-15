FROM python:3.6-alpine

RUN pip install --upgrade pip
RUN pip install gunicorn

ENV INSTALL_DIR /home/flask-celery-example
RUN mkdir -p $INSTALL_DIR
WORKDIR $INSTALL_DIR

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY config.py manage.py ./

EXPOSE 8000
USER nobody
ENTRYPOINT ["gunicorn"]
CMD ["--workers=1", "--bind=0.0.0.0:8000", "manage:app"]