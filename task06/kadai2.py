#coding:utf-8
import requests
import pprint

def get_api(keyword, url):
    payload = {
        'applicationId': 1094782773139302380,
        'hits': 30, #一度のリクエストで返してもらう最大個数（MAX30)
        'keyword': keyword,
        'page':1, #何ページ目か
        'postageFlag':1, #送料込みの商品に限定
        }
    r = requests.get(url, params=payload)
    return r.json()

def check_Data(json):
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    print("_/_/_/_/_/_/_/_/_/構造確認_/_/_/_/_/_/_/_/_/")
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

    pprint.pprint(json, depth=2, compact=True)

    total = int(json['count'])
    Max = total/30 + 1
    print("【num of item】",total)
    print("【num of page】",Max)

    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

    data = json['Products'][0]
    pprint.pprint(data, depth=2, compact=True)

    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

def print_Json(json):
    counter = 0
    for i in json['Products']:
        counter = counter + 1
        item = i['Product']
        name = item['productName']
        print('【No.】'+ str(counter))
        print('【Name】' + str(name[:30]) + '...')
        print('【maxPrice】' + '¥' +str(item['maxPrice']))
        print('【minPrice】' + '¥' +str(item['minPrice']))


def main():
    keyword = "鬼滅"
    url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    json = get_api(keyword, url)

 #   check_Data(json)
    print_Json(json)



main()