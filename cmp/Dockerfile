FROM python:3.11-slim-buster
ARG APPNAME

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY $APPNAME $APPNAME
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /$APPNAME

ENV ENV_APP $APPNAME
RUN chown -Rv www-data:www-data "/$ENV_APP"

CMD /usr/local/bin/gunicorn --bind 0.0.0.0:8000 --user www-data ${ENV_APP}.wsgi
