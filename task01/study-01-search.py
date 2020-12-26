# 検索ツールサンプル
# これをベースに課題の内容を追記してください

import csv
import pandas as pd

# 検索ソース
source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]


# 検索ツール
def search():
    print('初期値:{}'.format(source))
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    # 課題1
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        # 課題2
        print('{}は登録されていません'.format(word))
        # 課題3
        print('新たに追加します')
        source.append(word)
        print('追加後:{}'.format(source))


# 課題4
def search_csv(url: str):
    with open(url) as fileData:
        reader = csv.reader(fileData)
        for row in reader:
            print('csvファイルの初期中身は{}です'.format(row))
            csv_data = row

    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    if word in csv_data:
        print('{}は存在します。'.format(word))
    else:
        print('{}は存在しません。'.format(word))

        # 課題5
        ask_if_append = input('新たに{}を追加しますか？[y/N]'.format(word)).lower()
        if ask_if_append in ['y', 'ye', 'yes']:
            print('{}をファイルに追加します。'.format(word))
            with open(url, 'a') as csvData:
                writer = csv.writer(csvData, quoting=csv.QUOTE_ALL)
                writer.writerow([word])
            with open(url) as readData:
                print('csvファイルの書き込み後の中身は{}です'.format(readData.read()))
        elif ask_if_append is ['n', 'no']:
            print('{}を保存しませんでした。'.format(word))
        else:
            print('不正な値が入力されました。')


# +アルファの課題
def search_detail_csv(url: str):
    panda_data_frame = pd.read_csv(url, index_col=0)
    print(panda_data_frame.keys())
    name_list = tuple(panda_data_frame.index)
    name = input(f'{name_list}、だれの詳細データをみたいですか？')
    if name in name_list:
        print('一致データがありました。')
        hair_color = panda_data_frame.at[name, 'HairColor']
        move = panda_data_frame.at[name, 'Moves']
        print(f"髪の色:{hair_color}, 必殺技:{move}")
    else:
        print('一致するデータは存在しませんでした。')



if __name__ == "__main__":
    print('# 課題1-5')
    search_csv('kimetsuData.csv')
    print('# +アルファの課題')
    search_detail_csv('kimetsuDetailData.csv')
