import os

from motor.motor_asyncio import AsyncIOMotorClient


async def create_db_vea_and_insert_products(products, mongodb_uri=None):
    if mongodb_uri is None:
        mongodb_uri = os.getenv("MONGODB", "mongodb://localhost:27017")

    client = AsyncIOMotorClient(mongodb_uri)
    db = client["db_vea"]
    collection = db["products"]

    if not products:
        client.close()
        return 0

    result = await collection.insert_many(products)
    client.close()
    return len(result.inserted_ids)
