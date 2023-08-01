import requests
from requests.api import head
import csv
import json

#list endpoint
# https://uem.bukitmakmur.com:8383/api/1.4/inventory/compdetailssummary?resid=43260


#untuk login get token
apiLogin = ''  #Masukin Endpoint login disini cuy
headLogin = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
}

params = {
  "username": "Input Username disini ----------",
  "password": "Input password disini -----------"
}

resp = requests.post(apiLogin, headers = headLogin ,data=json.dumps(params))
tokennya = json.loads(resp.text)['token']

if resp.status_code != 200:
  print('error: ' + str(resp.status_code))
else:
  print('token: ' + str(tokennya))
  print('Success')
 


#=============================================================================
#untuk get Data
apiDetailRecord = 'http://localhost:8000/api/v1/berita/getBerita/' 
#detail record
apiCountRecord = 'http://localhost:8000/api/v1/berita/getBerita/' 
#check jlmh record

headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
  "Authorization": str(tokennya) #dapetin token sik diatas
}


#=============================================================================
#Count Record data 
response = requests.request("GET", apiCountRecord, headers=headers, data={})
data_json  = response.json()
total_data = len(data_json['data'])
print(total_data)


#=============================================================================
#convert to CSV file
with open ('Buma/berita.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['id','judul','kategori','deskripsi','gambar','user']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  # ================
  idplus = 1
  jlmhrecord = total_data #Jumlah datanya 
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

#=============================================================================
#Convert to JSON file
with open('Buma/data.json', 'w') as outfile:
  idplus = 0
  cok = []
  jlmhrecord = total_data  #jumlah datanya 
  for idplus in range(jlmhrecord):
    idplus += 1
    valueId = {'id': idplus}
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json()

    cok = cok + myjson['data']

  json.dump(cok, outfile)
  print("Done JSON bg")



