FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HEADLESS=true
ENV PYTEST_WORKERS=2
ENV BROWSER=chrome
ENV DOCKER_ENV=true

CMD ["python", "run_test.py"]