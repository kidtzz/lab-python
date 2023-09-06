import requests
from requests.api import head
import csv
import json



#=============contoh yg benernya=======
f = open('software.json')
data = json.load(f)
# print("status apa?", data[0]['status'])

with open ('test.csv','w', encoding='UTF8', newline='') as f:
  csvheader = ['user_name','managed_software_id','software_id','software_name','software_version','architecture','manufacturer_id','manufacturer_name']
  writer = csv.writer(f)
  writer.writerow(csvheader)
  idplus = 1

  jlmhrecord = 1 #Jumlah datanya 

  for idplus in range(jlmhrecord):
    ourdata = []
    for x in range(len(data)):
      if data['status'] == "success":
        # print(data[x]['message_response']['installedsoftware'])
        for i in data['message_response']['installedsoftware']:
          listing = [i['user_name'],i['managed_software_id'],i['software_id'],i['software_name'],i['software_version'],i['architecture'],i['manufacturer_id'],i['manufacturer_name']]
          writer.writerows([listing])
        # for i in data:
        #   listing = [i['message_response']['compdetailssummary']['asset_summary']['commercial_software'],i['message_response']['compdetailssummary']['computer_os_summary']['os_name'],i['message_response']['compdetailssummary']['computer_summary']['computer_name']]
        # ourdata.append(listing)
        # writer.writerows(ourdata)
      elif data[x]['status'] == "error":
        print("skip id ke - ", idplus)
print("Done CSV")


#  for idplus in range(jlmhrecord):
#     ourdata = []
#     for i in data['message_response']['installedsoftware']:
#       listing = [i['user_name'],i['software_name']]
#       writer.writerows([listing])
#     break