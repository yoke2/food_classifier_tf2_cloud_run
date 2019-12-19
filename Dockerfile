FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install packaging

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app app/

RUN python app/server.py

ENV PORT 8080

CMD ["python", "app/server.py", "serve"]
