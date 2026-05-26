import json
import os


def save_products_json(products, output_path=None):
    if output_path is None:
        output_path = os.getenv("JSON_OUTPUT", "products.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=2)

    return output_path
