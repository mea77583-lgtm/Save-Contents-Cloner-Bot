import os
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(os.environ.get('API_ID', "22557267"))
    API_HASH = os.environ.get('API_HASH', "cc74170e9c8e195c193d35953affe086")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "8211914636:AAF-IvkGHSc8N-PR66cQKM9QJ9I9SQJTRF8")
    AUTH_USER_ID = int(os.environ.get('AUTH_USER_ID', "1968724476"))
    
class Database:
    REDIS_HOST = os.environ.get('REDIS_HOST', "http://redis-10662.c82.us-east-1-2.ec2.redns.redis-cloud.com:10662") # Example: ec2.redns.redis-cloud.com, local-elephant-58690.upstash.io
    REDIS_PORT = int(os.environ.get('REDIS_PORT', "10662")) #Example 8080, 47384
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', "kEz1iVIEmvQfDLxt3uw2FK1jPRp4THby")
