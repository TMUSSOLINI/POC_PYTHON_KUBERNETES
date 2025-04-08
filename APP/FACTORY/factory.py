import asyncmy
import os
from dotenv import load_dotenv


load_dotenv()

class ConnectionDB:

    async def connection_db(self):
        try:
            return await asyncmy.connect(
                host=os.getenv("DATABASE_HOST_API"),
                user=os.getenv("DATABASE_USER_API"),
                password=os.getenv("DATABASE_PASSWORD_API"),
                db=os.getenv("DATABASE_NAME_API")
            )
        except Exception as e:
            raise Exception(f"Falha na conexão: {e}")