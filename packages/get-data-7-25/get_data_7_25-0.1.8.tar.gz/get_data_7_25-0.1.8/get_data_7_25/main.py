import sys
import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from get_data_7_25.api.get_api import search_booklog_ranking
from get_data_7_25.book.get_book import book
from get_data_7_25.book.bunko.get_bunko import bunko
from get_data_7_25.book.tankoubon.get_tankoubon import tankoubon

async def main_get():
    async def collect_data(search_func, limit=None):
        data = []
        async for item in search_func:
            data.append(item)
            if limit and len(data) >= limit:
                break
        # return data
        return {
            "data": data
        }

    get_api = collect_data(search_booklog_ranking())
    # get_api = api1()
    get_book = book()
    get_bunko = bunko()
    get_tankoubon = tankoubon()

    resuluts = await asyncio.gather(
        get_api,
        get_book,
        get_bunko,
        get_tankoubon
    )
    fetched_api, fetched_book, fetched_bunko, fetched_tankoubon = resuluts
    # fetched_book, fetched_bunko, fetched_tankoubon = resuluts
    fetch_api = fetched_api['data']
    fetch_book = fetched_book['book']
    fetch_bunko = fetched_bunko['bunko']
    fetch_tankoubon = fetched_tankoubon['tankoubon']
    print("fetched_data", {
        "data": fetch_api,
        "book": fetch_book,
        "bunko": fetch_bunko,
        "tankoubon": fetch_tankoubon
    })
    return {
        "data": fetch_api,
        "book": fetch_book,
        "bunko": fetch_bunko,
        "tankoubon": fetch_tankoubon
    }

if __name__ == "__main__":
    asyncio.run(main_get())