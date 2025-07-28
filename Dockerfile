FROM alpine:latest

RUN apk add --no-cache bash curl ca-certificates python3 py3-pip nodejs npm git build-base libffi-dev openssl-dev python3-dev fish postgresql-dev


# Instalar Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# Crear entorno virtual para instalar reflex y dependencias
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR "/app/web"

# Copiar requirements.txt
COPY "./app/web/requirements.txt" ./requirements.txt

RUN pip install -r ./requirements.txt

# No ejecutar reflex init porque ya tienes el proyecto

EXPOSE 3000
EXPOSE 8000


