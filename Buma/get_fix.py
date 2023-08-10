import requests
import csv
import json


apiDetailRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/inventory/compdetailssummary' 

tokenApi ='E572ADE0-4888-426B-BA3C-DBA6680F3296'
headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
  "Authorization": tokenApi 
}

#save csv
with open ('data-buma.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['commercial_software','os_name','computer_name']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  idplus = 43250
  jlmhrecord = 43260 #edit-jumlah record

  for i in range(idplus, jlmhrecord):
    valueId = {'resid': idplus}
    print("hit ke2?", idplus)
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json() 
    ourdata = []
    for x in range(len(myjson)):
      if myjson['status'] == "success":
        for i in myjson:
          listing = myjson['message_response']['compdetailssummary']['asset_summary']['commercial_software'], myjson['message_response']['compdetailssummary']['computer_os_summary']['os_name']
          ourdata.append(listing)
          writer.writerows(ourdata)
          print("perulangan ke?",idplus)
          break
        break
      elif myjson['status'] == "error":
        print("skip id ke - ", idplus)
        break
      else:
        break
    idplus += 1
print("Done CSV")
