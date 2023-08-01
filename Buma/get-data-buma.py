import requests
from requests.api import head
import csv
import json

#Login Get Token
apiLogin = 'https://uem.bukitmakmur.com:8383/api/1.4/desktop/authentication' 
headLogin = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
}
params = {
    "username":"uem.admin",
    "password":"QWRtaW5VRU04OTAqKCk=",
    "auth_type":"local_authentication"
}

resp = requests.request("POST", apiLogin, params={params}, headers = headLogin, data={})
generate = resp.json()
tokennya = generate['message_response']['authentication']['auth_data']['auth_token']
# tk='E572ADE0-4888-426B-BA3C-DBA6680F3296'

if resp.status_code != 200:
  print('error: ' + str(resp.status_code))
else:
  print('token: ' + str(tokennya))
  print('Success')

#GetAllData
apiDetailRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/inventory/compdetailssummary' 
#GetByID
apiCountRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/som/computers' 

headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
  "Authorization": str(tokennya) 
}

#Count Record data 
response = requests.request("GET", apiCountRecord, headers=headers, data={})
data_json  = response.json()
total_data = data_json['message_response']['total']
print(total_data)


#Ini masih perlu di edit scirptya soalnya id.nya tidak pasti 
with open ('test.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['commercial_software','os_name','computer_name']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  idplus = 1
  jlmhrecord = 1 #ini gmn caranya biar increment trus break
  for idplus in range(jlmhrecord):
    idplus += 1
    valueId = {'resid': idplus}
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json() 
    # bagian sini perlu diambahi kondisi
    #jika response status = 200 dia append masuk ke row CSV
    #jika response status = error maka skip aj tidak masuk row csv lanjut ID.nya
    #jika jmlh request = 2000 maka dia berhenti

    if response.status_code == 200:
      ourdata = []
      for x in myjson:
        listing = [x['message_response']['compdetailssummary']['asset_summary']['commercial_software'],x['message_response']['compdetailssummary']['computer_os_summary']['os_name'],x['message_response']['compdetailssummary']['computer_summary']['computer_name']]
      ourdata.append(listing)
    else:
      print('Skipp next id ',idplus)
    writer.writerows(ourdata)
print("Done CSV")





















#===================contoh yg benernya=======

#Contoh====
# f = open('buma_token_get.json.json')
# data = json.load(f)
# ah = data
# print(ah['message_response']['authentication']['auth_data']['auth_token'])


# Parsing to CSV =======
# f = open('buma_getid.json')
# data = json.load(f)

# with open ('test.csv','w', encoding='UTF8', newline='') as f:
#   csvheader = ['tes1','tes2','tes3']
#   writer = csv.writer(f)
#   writer.writerow(csvheader)
#   idplus = 1
#   jlmhrecord = 1 #Jumlah datanya 
#   for idplus in range(jlmhrecord):
#     ourdata = []
#     for x in data:
#       listing = [x['message_response']['compdetailssummary']['asset_summary']['commercial_software'],x['message_response']['compdetailssummary']['computer_os_summary']['os_name'],x['message_response']['compdetailssummary']['computer_summary']['computer_name']]
#     ourdata.append(listing)
#   writer.writerows(ourdata)
# print("Done CSV")