# Usa imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia o código do servidor
COPY servidor.py .

# Expõe a porta
EXPOSE 5000

# Comando para rodar o servidor
CMD ["python","-u", "servidor.py"]