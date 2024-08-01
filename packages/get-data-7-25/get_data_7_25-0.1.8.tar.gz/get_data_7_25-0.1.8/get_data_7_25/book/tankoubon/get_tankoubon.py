from ...api.get_api import api1
async def tankoubon():
    getting_api = await api1()
    getting_api = getting_api['data']
    # getting_api = "kari[tankoubon]"
    print("get_tankoubon + getting_api", getting_api)
    return {
        "tankoubon": f"tankoubon + {getting_api}"
    }