#!/usr/bin/env python3
import os
import json
import requests

hostname = "mohit614.ddns.net" #example
response = os.system("ping -c 1 " + hostname)

def post_message(msg):
    WEBHOOK_URI = 'https://hooks.chime.aws/incomingwebhooks/2fb4b548-78a7-43cf-b63c-b15fd70e180f?token=UExHZkZwSlV8MXxJLWNCa1hjQUhzZ3BfR2hMTWN2cjdqV3VNNmJ3WkhjRzRDUFlxNU1NaXFr'
    response = None
    try:
        response = requests.post(
            url=WEBHOOK_URI,
            json={"Content": msg})
        return json.loads(response.text)
    except:
        return response.tex

temp=0
count1=0
count2=0
#and then check the response...
while 1==1:
    response = os.system("ping -c 1 " + hostname)
    if response == 0 and temp != response:
      message = '/md @msinghva , light came back, yahhh!!!'
      count2==0;
      count1+=1;
      if count1 == 4:
        temp = response
        post_message(message)
        count1=0
    if response != 0 and temp != response:
      count1==0;
      count2+=1
      message = '/md @msinghva , Bad news...light gone'
      if count2==4:
        temp=response
        post_message(message)
        count2=0
