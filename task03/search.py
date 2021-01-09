import pandas as pd

### デスクトップアプリ作成課題
def kimetsu_search(word):
    # 検索対象取得
    df=pd.read_csv("./source.csv")
    source=list(df["name"])
    # 検索
    if word in source:
        return True
    else:
        return False

def add_to_kimetsu(word):
    # 検索対象取得
    df=pd.read_csv("./source.csv")
    source=list(df["name"])
    source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./source.csv",encoding="utf_8-sig")
    print(source)