MISTRAL_API_KEY = "your_api_key_here"
# MONGO_URI = "mongodb://localhost:27017/" # Local MongoDB connection
MONGO_URI = "mongodb+srv://hatmatty:mLT7nUkr6OLdc0xW@cluster0.enmtn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "cdc_database"
COLLECTION_NAME = "datasets"
CONFIG_COLLECTION = "config"

# Automatically fetch datasets on app start
AUTO_FETCH_ON_START = True  # Implementer should change this if updates are needed