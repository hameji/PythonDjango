#1 変数の使い方

name1 = 'ねずこ'
name2 = 'ぜんいつ'

def printAlliance():
    print('「' + name1 + '」と「' + name2 + '」は仲間です')

printAlliance()

#2 if文の使い方

name2 = 'むざん'

def printEnemy():
    if name2 == 'むざん':
        print('仲間ではありません')

printEnemy()

#3 配列の使い方
character_list = ['たんじろう', 'ぎゆう', 'ねずこ', 'むざん']

def addCharacter():
    character_list.append('ぜんいつ')
    print(character_list)

addCharacter()

#4 for文の使い方

def printListMember():

    for character in character_list:
        print(character)

printListMember()

#5 関数の使い方

#6 引数を使う関数の使い方

def checkCharacter(name: str):
    if name in character_list:
        print(name + 'はリストに含まれます。')
    else:
        print(name + 'はリストに含まれません。')

checkCharacter('むざん')