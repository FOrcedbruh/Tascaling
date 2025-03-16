FROM python:3.12-slim-bullseye



ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1

ARG UID=65534
ARG GID=65534

WORKDIR /

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        gcc \
        libc-dev \
        libpq-dev \
        python-dev \
        libxml2-dev \
        libxslt1-dev \
        python3-lxml && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python3", "main.py"]