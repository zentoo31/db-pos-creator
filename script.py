import requests
from bs4 import BeautifulSoup

url = "https://www.plazavea.com.pe/"
url_api = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=C:/431/&_from=1&_to=50&O=OrderByScoreDESC&"


def getProductsAbarrotes(nro):

    all_products = []

    for i in range(0, int(nro), 50):
        end = min(i + 49, int(nro) - 1)

        response = requests.get(
            f"https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=C:/431/&_from={i}&_to={end}&O=OrderByScoreDESC&"
        )

        data = response.json()

        products = [
            {
                "id": p["items"][0]["itemId"],
                "name": p["items"][0]["name"],
                "brand": p["brand"],
                "brandId": p["brandId"],
                "description": p["metaTagDescription"],
                "categories": p["categories"],
                "imageUrl": p["items"][0]["images"][0]["imageUrl"],
                "price": p["items"][0]["sellers"][0]["commertialOffer"]["Installments"][
                    0
                ]["Value"],
            }
            for p in data
        ]

        all_products.extend(products)

    print(all_products)
    print("numero de elementos: " + str(len(all_products)))


def verPag():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)


def veaStatus():
    if requests.get(url):
        print("Plaza vea está en línea correctamente!")
    else:
        print("Plaza vea está caído")
