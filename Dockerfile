FROM alpine:latest
COPY ./app/web /app/web

# Instalar dependencias
RUN apk add --no-cache \
    bash \
    curl \
    ca-certificates \
    python3 \
    py3-pip \
    nodejs \
    npm \
    git \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev \
    fish \
    postgresql-dev \
    && rm -rf /var/cache/apk/*

# Crear estructura con permisos adecuados
RUN adduser -D devuser && \
    mkdir -p /app/web && \
    chown -R devuser:devuser /app && \
    # Permisos especiales para .web
    mkdir -p /app/web/.web && \
    chown -R devuser:devuser /app/web/.web && \
    chmod -R u+rw /app/web/.web

# Instalar Bun como devuser
USER devuser
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/home/devuser/.bun/bin:${PATH}"

# Configurar entorno virtual Python
RUN python3 -m venv /home/devuser/venv
ENV PATH="/home/devuser/venv/bin:$PATH"

WORKDIR "/app/web"

# Copiar requirements e instalar dependencias
COPY --chown=devuser:devuser "./app/web/requirements.txt" ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 3000 8000