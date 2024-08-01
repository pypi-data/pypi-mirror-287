from bs4 import BeautifulSoup as bs
import urllib.parse as up
import datetime
import re
import aiohttp

HOST="booklog.jp"
URL="https://"+HOST
BASE_URL=URL+"/ranking/weekly"
HEADERS={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# urlからisbnを抽出する関数
import re

def extract_number(input_string):
    pattern = r'/item/1/(\d+)'
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    else:
        return None

# priceから数字を抽出する関数
def extract_numbers(text):
  return re.findall(r"\d+", text)

# rakuten_apiからデータを取得する関数
async def get_book_info(get_isbn):
    book_data = get_isbn
    if book_data:
        # print("データを取得しました:", book_data)
        return book_data
    else:
        print("データの取得に失敗しました。")
        return None

class SearchType:
  book = "book"
  bunko = "bunko"
  shinsho = "shinsho"
  comic = "comic"
  honour = "honour"

today=datetime.date.today()
from datetime import datetime, timedelta
from calendar import Calendar

date=datetime.now() - timedelta(hours=12)
calendar = Calendar(firstweekday=0)
month_calendar = calendar.monthdays2calendar(date.year, date.month)

count=1
for week in month_calendar:
  for day in week:
    if day[0] == date.day:
      break
  else:
    count+=1
    continue
  break

year=str(today.year)
month=date.month
if month == 0:
  year -= 1
  month = 12
elif month == 1:
  month = "01"
elif month == 2:
  month = "02"
elif month == 3:
  month = "03"
elif month == 4:
  month = "04"
elif month == 5:
  month = "05"
elif month == 6:
  month = "06"
elif month == 7:
  month = "07"
elif month == 8:
  month = "08"
elif month == 9:
  month = "09"
week = count

async def _search(type_=SearchType.book):
    async with aiohttp.ClientSession() as session:
        SEARCH_URL=BASE_URL + "/" + str(year) + str(month) + "/" + str(count) + "/" + type_
        # print("SEARCH_URL", SEARCH_URL)
        async with session.get(SEARCH_URL, headers=HEADERS) as response:
            return await response.text()

async def toData(l):
  get_isbn = str(extract_number(l.select_one(".thumb").find("a").get("href")))
  book_info = await get_book_info(get_isbn)
  return {
    "bookin": book_info
  }

async def getData(soup):
  kari1 = soup.select_one(".autopagerize_page_element.t20M")
  # print("kari1",kari1)
  kari2 = kari1.select_one(".ranking-list")
  for l in kari2.select(".clearFix")[:1]:
    yield await toData(l)
async def search_booklog_ranking(type_=SearchType.book):
  text= await _search(type_)
  soup= bs(text,"html.parser")
  async for data in getData(soup):
    yield data

# async def api1():
#     data = await list(search_booklog_ranking())
#     print("data[get_api]",data)
#     return {
#       "data": data
#     }


async def api1():
    data = []
    async for item in search_booklog_ranking():
        data.append(item)
    print("data[get_api]", data)
    return {
        "data": data
    }