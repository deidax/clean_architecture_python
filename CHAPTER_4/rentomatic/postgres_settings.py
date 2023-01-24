import os
from dotenv import load_dotenv
load_dotenv()


postgres_connexion = {
    'dbname':os.getenv('POSTGRES_DB', ''),
    'user':os.getenv('POSTGRES_USER', ''),
    'password':os.getenv('POSTGRES_PASSWORD', ''),
    'host':'localhost'
}