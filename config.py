import os
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH', "")
    BOT_TOKEN = ")
    AUTH_USER_ID = int(os.environ.get('AUTH_USER_ID', "16"))
    
class Database:
    REDIS_HOST = os.environ.get('REDIS_HOST', "http://redis-10662.c82.us-:10662") # Example: ec2.redns.redis-cloud.com, local-elephant-58690.upstash.io
    REDIS_PORT = int(os.environ.get('REDIS_PORT', "10662")) #Example 8080, 47384
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', "kEz1iVIEmvQfHby")
