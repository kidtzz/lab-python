import requests
import csv
from requests.api import head

url = 'http://localhost:8000/api/v1/berita/getBerita/'

headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json"
}

with open ('berita.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['id','judul','kategori','deskripsi','gambar','user']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  # ===============
  idplus = 1
  for idplus in range(10):
    idplus += 1
    valueId = {'id': idplus}
    response = requests.request("GET", url, params=valueId, headers=headers, data={})
    myjson  = response.json();
    # ===============  
    ourdata = []
    for x in myjson['data']:
      listing = [x['id'],x['judul'],x['kategori'],x['deskripsi'],x['gambar'],['user']]
      ourdata.append(listing)
  # ===============
    writer.writerows(ourdata)
    
print('done bg')