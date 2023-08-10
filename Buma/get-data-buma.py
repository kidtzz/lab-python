
import requests
from requests.api import head
import csv
import json

#Login Get Token
# apiLogin = 'https://uem.bukitmakmur.com:8383/api/1.4/desktop/authentication' 
# headLogin = {
#   "Accept" : "application/json",
#   "Content-type" : "application/json",
# }
# params = {
#     "username":"uem.admin",
#     "password":"QWRtaW5VRU04OTAqKCk=",
#     "auth_type":"local_authentication"
# }

# resp = requests.request("POST", apiLogin, params={params}, headers = headLogin, data={})
# generate = resp.json()
# tokennya = generate['message_response']['authentication']['auth_data']['auth_token']

# if resp.status_code != 200:
#   print('error: ' + str(resp.status_code))
# else:
#   print('token: ' + str(tokennya))
#   print('Success')

#=======================================================================

#GetAllData
apiDetailRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/inventory/compdetailssummary' 
#GetByID
# apiCountRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/som/computers' 

par_token='E572ADE0-4888-426B-BA3C-DBA6680F3296'

headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
  "Authorization": par_token  #change par_token
}

#Count Record data 
# response = requests.request("GET", apiCountRecord, headers=headers, data={})
# data_json  = response.json()
# total_data = data_json['message_response']['total']
# print(total_data)

#save csv
with open ('data-buma.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['commercial_software','os_name','computer_name']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  idplus = 0

  jlmhrecord = 10000 #edit-jumlah record
  for idplus in range(jlmhrecord):
    valueId = {'resid': idplus}
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json() 
    ourdata = []
    for x in range(len(myjson)):
      if myjson[x]['status'] == "success":
        for i in myjson:
          listing = [i['message_response']['compdetailssummary']['asset_summary']['commercial_software'],i['message_response']['compdetailssummary']['computer_os_summary']['os_name'],i['message_response']['compdetailssummary']['computer_summary']['computer_name']]
        ourdata.append(listing)
        writer.writerows(ourdata)
      elif myjson[x]['status'] == "error":
        print("skip id ke - ", idplus)
    idplus += 1
print("Done CSV")

# bagian sini perlu diambahi kondisi
#jika response status = 200 dia append masuk ke row CSV
#jika response status = error maka skip aj tidak masuk row csv lanjut ID.nya
#jika jmlh request = 2000 maka dia berhenti













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