FROM python:3.12-slim-bullseye



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_OFF=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

ARG UID=65534
ARG GID=65534

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python3", "main.py"]