FROM python:3.11.2-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app

CMD ["python", "-m", "app.main"]