import requests
import csv
from requests.api import head
import json

apiDetailRecord = 'http://localhost:8000/api/v1/berita/getBerita/'
apiCountRecord = 'http://localhost:8000/api/v1/berita/getBerita/'

headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json"
}

#Count Record data 
response = requests.request("GET", apiCountRecord, headers=headers, data={})
data_json  = response.json()
total_data = len(data_json['data'])
print(total_data)

#convert to CSV file
with open ('berita.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['id','judul','kategori','deskripsi','gambar','user']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  # ================
  idplus = 1
  jlmhrecord = total_data #isi-jumlah datanya dengan API Count
  for idplus in range(jlmhrecord):
    idplus += 1
    valueId = {'id': idplus}
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json()
    # ===============  
    ourdata = []
    for x in myjson['data']:
      listing = [x['id'],x['judul'],x['kategori'],x['deskripsi'],x['gambar'],x['user']]
      ourdata.append(listing)
  # ===============
    print(ourdata)
    writer.writerows(ourdata)
  print("Done CSV bg")


#Convert to JSON file
with open('data.json', 'w') as outfile:
  idplus = 0
  cok = []
  jlmhrecord = total_data #isi-jumlah datanya dengan API Count
  for idplus in range(jlmhrecord):
    idplus += 1
    valueId = {'id': idplus}
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json()

    cok = cok + myjson['data']

  json.dump(cok, outfile)
  print("Done JSON bg")