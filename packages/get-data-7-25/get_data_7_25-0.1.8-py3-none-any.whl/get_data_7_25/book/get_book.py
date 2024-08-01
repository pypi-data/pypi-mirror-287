from ..api.get_api import api1

async def book():
    getting_api = await api1()
    getting_api = getting_api['data']
    # getting_api = "kari[book]"
    print("getting_api", getting_api)
    return {
        "book": f"book + {getting_api}"
    }