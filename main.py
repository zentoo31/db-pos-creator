import argparse

import script

parser = argparse.ArgumentParser(
    description="Herramienta para crear base de datos para proyectos de inventario, POS, etc. Se usa Plaza Vea como target scraper"
)
parser.add_argument(
    "--status", action="store_true", help="Ver el estado de la web de plaza vea"
)
parser.add_argument("--pag", action="store_true", help="Ver la pag de plaza vea")
parser.add_argument("--products", action="store", help="Ver los productos a importar")

args = parser.parse_args()

if args.status:
    script.veaStatus()
if args.pag:
    script.verPag()
if args.products:
    script.getProductsAbarrotes(args.products)
