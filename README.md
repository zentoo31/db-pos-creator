# DB POS Creator

Este programa scrapea la web de Plaza Vea (https://www.plazavea.com.pe/) para obtener productos de abarrotes y permite crear una base de datos con esos productos según la base de datos elegida.

Actualmente soporta MongoDB.

Uso rápido:

1. Ver productos en consola: `python main.py --products 100`
2. Crear la base de datos e insertar en MongoDB: `python main.py --products 100 --mongodb`

El string de conexión se toma de la variable de entorno `MONGODB` (por defecto `mongodb://localhost:27017`).
