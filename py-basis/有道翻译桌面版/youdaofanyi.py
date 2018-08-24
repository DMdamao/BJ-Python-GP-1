'''
The data of:2018/03/16
author:北冥神君
content:实现有道翻译实现翻译
Last update time:2018/03/16
version:1.0
'''
#导入模块
import requests       #网络请求模块
import time           #时间模块
import random         #随机模块
import hashlib        #哈希加密模块
#面向对象编程
class YoudaoTranslation:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'   #翻译接口
        #反爬
        self.header = {'Host': 'fanyi.youdao.com',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Accept-Encoding': 'gzip, deflate',
                        'Referer': 'http://fanyi.youdao.com/',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Length': '201',
                        'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=154739022@10.169.0.84; JSESSIONID=aaaEHwB7WYj7-9S0nnSiw; ___rl__test__cookies=1521160027414; OUTFOX_SEARCH_USER_ID_NCOO=2132109642.9472575; fanyi-ad-id=41685; fanyi-ad-closed=1',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache'}

    #翻译函数
    def get_fanyi(self,text):
        self.data = self.get_js(text)
        self.response = requests.post(url=self.url, data=self.data, headers=self.header)
        if len(self.response.json()) ==4:
            print('翻译原文===>:',self.response.json()['translateResult'][0][0]['tgt'])
            print('译文结果===>:', self.response.json()['translateResult'][0][0]['src'])
            print('\n')
            #打印完整的解释
            for i in range(1,len(self.response.json()['smartResult']['entries'])):
                print('译文解释',i,'===>:',self.response.json()['smartResult']['entries'][i])
        else:print('未找到翻译')

    # js加密参数解法
    def get_js(self,i):
        self.content = i
        self.u = 'fanyideskweb'
        self.d = self.content#查询文本内容
        self.timekey = str(int(time.time() * 1000) + random.randint(1, 10))#时间戳+随机数
        self.c = 'ebSeFb%=XZ%T[KZ)c(sy!'            #2.1版本钥匙'aNPG!!u6sesA>hBAW1@(-'使用3.0版本钥匙可用.D : "ebSeFb%=XZ%T[KZ)c(sy!"
        self.key = hashlib.md5((self.u + self.d + self.timekey + self.c).encode('utf-8')).hexdigest()#加密数据
        #构造表单数据
        self.form = {'action':'FY_BY_REALTIME',
                    'client':'fanyideskweb',
                    'doctype':'json',
                    'from':'AUTO',
                    'i':self.content,
                    'keyfrom':'fanyi.web',
                    'salt':self.timekey,
                    'sign':self.key,
                    'smartresult':'dict',
                    'to':'AUTO',
                    'typoResult':'false',
                    'version':'2.1'
        }
        return self.form

#本模块测试
if __name__ == '__main__':
    while True:
        query = YoudaoTranslation()
        text = input("(按Q退出本程序)请输入你的要翻译的文本：\n")
        if text == 'Q':
            break
        query.get_fanyi(text)





