import requests
import json

URL_CAT_PV = "https://www.plazavea.com.pe/api/catalog_system/pub/category/tree/8"

r = requests.get(URL_CAT_PV)
lst_cat = json.loads(r.text)
print(lst_cat)


URL_CAT_METRO = 'https://www.metro.pe/api/catalog_system/pub/category/tree/8'

r = requests.get(URL_CAT_METRO)
lst_cat = json.loads(r.text)
print(lst_cat)
