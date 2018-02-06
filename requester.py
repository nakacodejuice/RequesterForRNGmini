# -*- coding: utf-8 -*-
import json
import requests
from requests.auth import HTTPBasicAuth  
from zeep import Client
from zeep.transports import Transport
from requests import Session

host = 'http://127.0.0.1:8000/'
WSDLRNG = 'http://localhost/RNG/ws/dataexchange.1cws?wsdl'
loginRNG = "Admin"
passRNG = "123"

headers = {'content-type': 'application/json'}
message = {'event':'GetNewRequest'}
res = requests.post(host+'rest/', json=message, headers=headers)
received_json_data = json.loads(res.content.decode("utf-8-sig"))
data = received_json_data['data']
isnext = received_json_data['isnext']
print (data)
#if(len(data)!=0):
session = Session()
session.auth = HTTPBasicAuth(loginRNG, passRNG)
transport_with_basic_auth = Transport(session=session)
client = Client(WSDLRNG,transport=transport_with_basic_auth)
res = client.service.ВыполнитьАлгоритмИПолучитьРезультат("Mob", '',False,False,True)