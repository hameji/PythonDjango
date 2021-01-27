import eel
import desktop
import pos

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def make_items():
    order = pos.main()
    return order

@ eel.expose
def fetch_item(item_code):
    order_list = []
    hasItem = pos.hasItem()
    if (hasItem) {
        eel.showOrder(order_list)
        price = 0
        eel.showTotalPrice(price)
    } else {
        eel.promptNoItem(item_code)
    }

@ eel.expose
def add_to_kimetsu(path, word):
    print("a")

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)
