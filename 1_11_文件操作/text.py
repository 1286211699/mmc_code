'''
该代码主要是整理
'''
import random
with open(r'E:\xuegod_code\1_11_文件操作\抽奖手机号.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        num = random.randrange(1,7)
        with open('data.txt','a',encoding='utf-8') as e:
            data = '''personArray.push({
                id: 546,
                image :"img/tx.png",
                thumb_image :"img/tx.png",
                name: "%s"
            });'''%(line.strip())+'\n'
            e.write(data)
