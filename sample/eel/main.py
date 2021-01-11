# pip install ellでインストールしたellをインポート
import eel
import numpy as np

# フォルダ構成で作ったwebファイルを読み込みます
eel.init("web")


## 以下はHTML側から呼び出せる
@eel.expose
def python_fuｎction(val):
    print(val + " from JavaScript")

@eel.expose
def python_function2():
    return "hello"

## eel.で直接呼び出せ得る
eel.js_function(np.random.rand(10).tolist())

eel.start("main.html")
