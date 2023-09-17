# Utilisez une image Python officielle en tant qu'image parente
FROM python:3.11-slim

# Définissez le répertoire de travail à /app
WORKDIR /app

# Copiez le contenu du répertoire actuel dans le conteneur à /app
COPY . /app

# Installez les dépendances spécifiées dans requirements.txt
RUN pip install -r requirements.txt

# Exposez le port 80 pour que FastAPI puisse écouter les requêtes HTTP
EXPOSE 80

# Définissez la commande pour lancer l'application FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
