#coding:utf-8
import requests
import pprint
import csv

def requestUrl(url):
    payload = {
        'applicationId': 1094782773139302380,
        'genreId': 100283, # 洋菓子
        'carrier': 0, # 0:PC, 1:mobile
        'page':1, #何ページ目か
        }
    r = requests.get(url, params=payload)
    return r.json()

def checkData(json):
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    print("_/_/_/_/_/_/_/_/_/構造確認_/_/_/_/_/_/_/_/_/")
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

    pprint.pprint(json, depth=2, compact=True)

    # total = int(resp['Items'])  <- これ働かなかったなぜ？
    # Max = total/30 + 1
    # print("【num of item】",total)
    # print("【num of page】",Max)

    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

    data = json['Items'][0]
    pprint.pprint(data, depth=2, compact=True)

    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

def parseJsontoList(json):
    ranking_list = []

    counter = 0
    for i in json['Items']:
        counter = counter + 1
        item = i['Item']
        rank = item['rank']
        name = item['itemName']
        print('【rank】'+ str(rank))
        print('【Name】' + str(name[:30]) + '...')
        rankData = [rank, name]
        ranking_list.append(rankData)
        if counter == 10:
            break

    return ranking_list

def add_to_csv_file(path, list):
    with open(path, mode='a', encoding="utf-8_sig") as file:
        writer = csv.writer(file)
        writer.writerow(list)

def main():
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    json = requestUrl(url)

    # checkData(json)

    list = parseJsontoList(json)
    add_to_csv_file('kadai3data.csv', list)
    

main()