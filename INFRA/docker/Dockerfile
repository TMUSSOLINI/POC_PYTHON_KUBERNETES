FROM python:3.11-slim-buster

WORKDIR /app

COPY ./APP/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./APP .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]