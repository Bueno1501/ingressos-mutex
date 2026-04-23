FROM python:3.11-slim

WORKDIR /app

COPY servidor.py .

EXPOSE 5000

CMD ["python","-u", "servidor.py"]
