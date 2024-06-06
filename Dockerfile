FROM mongo:latest

# Instalar wget e gnupg
RUN apt-get update && apt-get install -y wget gnupg

# Adicionar a chave pública do MongoDB
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

# Adicionar o repositório do MongoDB à lista de fontes
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Atualizar a lista de pacotes e instalar o cliente mongo
RUN apt-get update && apt-get install -y mongodb-org-shell

# Remover a linha de verificação de versão do Mongo
# RUN mongo --version
