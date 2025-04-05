
# Usa uma imagem oficial do Python com apt disponível
FROM Python 3.13.2

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    libdbus-1-dev \
    libglib2.0-dev \
    pkg-config \
    python3-dev \
    build-essential

# Cria diretório do app
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para iniciar seu app
CMD ["python", "cotacoes.py"]  # Altere para seu arquivo principal
