import requests
# API ENDPOINT
URL = "{API_ENDPOINT}/api/v1?token={TOKEN}&bank={KODE_BANK}&matauang={MATA_UANG}"
r = requests.get(url = URL)
data = r.json()
# tampilkan kurs jual bank BCA
print(data['jual'])
