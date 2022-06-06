FROM python:3.10-slim

ARG UNAME=appuser
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_ENV={$APP_ENV}

# Install pipenv and compilation dependencies
RUN apt update && apt install -y --no-install-recommends gcc netcat

COPY app/ /app

WORKDIR /app

RUN if [ -d "./venv" ] ; then \
    rm -rf venv ; \
    fi

RUN pip install -r requirements.txt

RUN chown -R $UNAME:$UNAME /app

USER $UNAME

RUN chmod +x start_app.sh

CMD bash start_app.sh
