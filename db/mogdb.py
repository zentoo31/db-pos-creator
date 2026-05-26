from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def mongodb():
    client = AsyncIOMotorClient(
        ""
    )
    
    db = client["db_vea"]