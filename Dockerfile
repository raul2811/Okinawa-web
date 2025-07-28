FROM alpine:latest

RUN apk add --no-cache bash curl ca-certificates python3 py3-pip nodejs npm git build-base libffi-dev openssl-dev python3-dev

RUN python3 -m ensurepip && pip3 install --upgrade pip setuptools wheel

# Instalar Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

RUN pip3 install reflex

WORKDIR /app

# Inicializar proyecto Reflex con plantilla 0 (blank)
RUN echo "0" | reflex init

# Expone puerto por defecto para reflex run
EXPOSE 3000

CMD ["reflex", "run"]
