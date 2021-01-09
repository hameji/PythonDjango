import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word):
    result = search.kimetsu_search(word)
    if result:
        eel.display_result(f"『{word}』は保存されいてます。")    
    else:
        eel.display_result(f"『{word}』は保存されていません。")
        eel.ask_if_append(word)

@ eel.expose
def add_to_kimetsu(word):
    search.add_to_kimetsu(word)
    eel.display_result(f"『{word}』をファイルに保存しました。")


    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)
