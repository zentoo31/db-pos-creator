import argparse
import asyncio

import script
from db import json as json_db
from db import mongodb

parser = argparse.ArgumentParser(
    description="Herramienta para crear base de datos para proyectos de inventario, POS, etc. Se usa Plaza Vea como target scraper"
)
parser.add_argument(
    "--status", action="store_true", help="Ver el estado de la web de plaza vea"
)
parser.add_argument("--pag", action="store_true", help="Ver la pag de plaza vea")
parser.add_argument("--products", action="store", help="Ver los productos a importar")
parser.add_argument(
    "--mongodb",
    action="store_true",
    help="Guardar productos en MongoDB (requiere --products)",
)
parser.add_argument(
    "--json",
    action="store_true",
    help="Guardar productos en products.json (requiere --products)",
)

args = parser.parse_args()

if args.status:
    script.veaStatus()
if args.pag:
    script.verPag()
if args.products:
    if args.mongodb or args.json:
        products = script.getProductsAbarrotes(args.products, show=False)
        if args.mongodb:
            inserted = asyncio.run(mongodb.create_db_vea_and_insert_products(products))
            print(f"Se insertaron {inserted} productos en db_vea.")
        if args.json:
            output_path = json_db.save_products_json(products)
            print(f"Se guardaron {len(products)} productos en {output_path}.")
    else:
        script.getProductsAbarrotes(args.products)
elif args.mongodb or args.json:
    print("Debes indicar --products <n> para importar.")
