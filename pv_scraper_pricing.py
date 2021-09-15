import requests
import json

URL_CAT = "https://www.plazavea.com.pe/api/catalog_system/pub/category/tree/8"

r = requests.get(URL_CAT)
lst_cat = json.loads(r.text)
print(lst_cat)
