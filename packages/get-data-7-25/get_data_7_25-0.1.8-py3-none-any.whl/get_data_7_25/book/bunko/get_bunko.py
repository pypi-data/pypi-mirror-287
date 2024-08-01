from ...api.get_api import api1
async def bunko():
    getting_api = await api1()
    getting_api = getting_api['data']
    # getting_api = "kari[bunko]"
    print("get_bunko + getting_api", getting_api)
    return {
        "bunko": f"bunko + {getting_api}"
    }