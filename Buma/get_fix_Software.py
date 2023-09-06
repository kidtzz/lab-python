import requests
from requests.api import head
import csv
import json


apiDetailRecord = 'https://uem.bukitmakmur.com:8383/api/1.4/inventory/installedsoftware' 

tokenApi ='E572ADE0-4888-426B-BA3C-DBA6680F3296'
headers = {
  "Accept" : "application/json",
  "Content-type" : "application/json",
  "Authorization": tokenApi 
}

#save csv
with open ('data-buma-software.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['user_name','managed_software_id','software_id','software_name','software_version','architecture','manufacturer_id','manufacturer_name']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  idplus = 43250
  jlmhrecord = 43270 #edit-jumlah record

  for i in range(idplus, jlmhrecord):
    valueId = {'resid': idplus}
    print("hit ke2?", idplus)
    response = requests.request("GET", apiDetailRecord, params=valueId, headers=headers, data={})
    myjson  = response.json() 
    ourdata = []
    for x in range(len(myjson)):
      if myjson['status'] == "success":
        for i in myjson[x]['message_response']['installedsoftware']:
          listing = [i['user_name'],i['managed_software_id'],i['software_id'],i['managed_software_id'],i['software_name'],i['software_version'],i['architecture'],i['manufacturer_id'],i['manufacturer_name']]
          writer.writerows([listing])
          break
        break
      elif myjson['status'] == "error":
        print("skip id ke - ", idplus)
        break
      else:
        break
    idplus += 1
print("Done CSV")


# for i in myjson:
#   listing = myjson['message_response']['installedsoftware']['user_name']
#   ourdata.append(listing)
#   writer.writerows(ourdata)