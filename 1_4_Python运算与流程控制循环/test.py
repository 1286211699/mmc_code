import requests

# with open('1.mp4','wb')  as f:
#     f.write(requests.get('http://qnvideo.ippzone.com/zyvd/a6/1a/8bd6-5093-11e9-b0d8-00163e0c0248').content)
url = 'http://diagnosis.ippzone.com/diagnosis/cdn/api?sign=622098b21f085d221e8f523b654093ec'
url2 = 'http://qnvideo.ippzone.com/'
# http://dlvideo.ippzone.com/zyvd/d6/d8/b5cd-5039-11e9-b0d8-00163e0c0248

headers = {
    'User-Agent': 'okhttp/3.11.0'
}
content = requests.get(url=url2,headers=headers)
print(content.text)
print(b'[17:46:57] root: \xe4\xbd\xa0\xe5\xa5\xbd'.decode())
