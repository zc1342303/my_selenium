# encoding:utf-8
import requests 
import base64
import json

'''
获取Token
'''
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Hv4xrhKiYV3SXHGcVR9seiPl&client_secret=1YBFxvgE8gi1uGm5TLWt0qYjnr4qGl84'
response = requests.get(host)
token_json = response.json()

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('/Users/zc/Downloads/getVerifyCode.jpeg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = token_json['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
result_json = response.json()
result = result_json['words_result'][0]['words']
print(result)