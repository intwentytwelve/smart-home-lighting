import requests
from nanoleafapi import Nanoleaf

def send_notice(event_name, key, text):
    url = "https://maker.ifttt.com/trigger/"+'notice_phone'+"/with/key/"+'cHfwbFfxP4F2Bm0EZ3oFJFgouwZ3aRDb8Ct5ta1SbYa'+""
    payload = "{\n    \"value1\": \""+text+"\"\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
 
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    if response.text=='Congratulations! You\'ve fired the notice_phone event':
        nl=Nanoleaf('192.168.0.108','GqOO9LTcPmhcjO26mjbtvcSaUwU3dd3v')
        nl.identify()
    #print(response.text)
 
text = "Please come to my office"
send_notice('notice_phone', 'cHfwbFfxP4F2Bm0EZ3oFJFgouwZ3aRDb8Ct5ta1SbYa', text)

