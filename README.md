# DB POS Creator

Este programa scrapea la web de Plaza Vea (https://www.plazavea.com.pe/) para obtener productos de abarrotes y permite crear una base de datos con esos productos según la base de datos elegida.

![Plaza Vea](img/images.png)

Actualmente soporta MongoDB y salida a JSON.

Uso rápido:

1. Ver productos en consola: `python main.py --products 100`
2. Crear la base de datos e insertar en MongoDB: `python main.py --products 100 --mongodb`
3. Guardar en JSON: `python main.py --products 100 --json`

El string de conexión se toma de la variable de entorno `MONGODB` (por defecto `mongodb://localhost:27017`).
El archivo JSON se guarda en `products.json` (configurable con `JSON_OUTPUT`).
