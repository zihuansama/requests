import requests

url = 'http://www.baidu.com'

response = requests.get(url = url)
response.encoding='utf-8'
print(response.text) #常用的

#网页源码
# print(response.url)
# print(response.content)#返回一个二进制数据 用的不多 用text 就行

# print(response.status_code)#响应 的状态码
# print(response.headers)