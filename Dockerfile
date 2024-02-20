FROM python:3.11.2-slim

WORKDIR /usr/src/appication

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["python", "-m", "app.main"]