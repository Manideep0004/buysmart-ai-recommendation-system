import os
import asyncio
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
uri = os.getenv('MONGO_URI')
print('MONGO_URI=', uri)

async def main():
    client = AsyncIOMotorClient(uri)
    try:
        result = await client.admin.command('ping')
        print('PING RESULT:', result)
    finally:
        client.close()

if __name__ == '__main__':
    asyncio.run(main())
