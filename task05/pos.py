import os, csv
import datetime as dt

NEW_LINE_CODE = "\r\n" if os.name == "nt" else "\n"

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

class Request:
    def __init__(self, item_code, item_amount):
        self.item_code = item_code
        self.item_amount = item_amount

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,request):
        self.item_order_list.append(request)

    def get_item_from_list(self, item_code):
        for item in self.item_master:
            if item.item_code == item_code:
                print("exists")
            else:
                print("not here")

        
    def view_item_list(self):
        for request in self.item_order_list:
            print(f"商品コード: { request.item_code }, 数量: { request.item_amount }")

    def get_order_list(self, money):
        total_price = 0
        data = ""
        for request in self.item_order_list:
            item_code = request.item_code
            for item in self.item_master:
                if item.item_code == item_code:
                    data += f"商品コード: {item.item_code}, 商品名: {item.item_name}, 金額: {item.price}, 数量: {request.item_amount}{NEW_LINE_CODE}" 
                    print(f"商品コード: {item.item_code}, 商品名: {item.item_name}, 金額: {item.price}, 数量: {request.item_amount}")
                    total_price += item.price * int(request.item_amount)
        data += f"合計金額は {total_price} 円 です。{NEW_LINE_CODE}"
        print(f"合計金額は {total_price} 円 です。")    
        data += f"お預り金は{money} 円です。{NEW_LINE_CODE}"
        print(f"お預り金は{money} 円です。")
        if total_price < money:
            change = money - total_price
            data += f"お釣りは{change}円となります。{NEW_LINE_CODE}"
            print(f"お釣りは{change}円となります。")
        else:
            shortage = total_price - money
            data += f"{shortage} 円不足しています。{NEW_LINE_CODE}"
            print(f"{shortage} 円不足しています。")
        return data

### 保存クラス
class ReceiptManager():

    def make_data_path():
        today_time = dt.datetime.now().strftime('%Y%m%d_%H%M%S') ## %H:%M:%S
        path = "receipt" + today_time + ".txt" 
        return path

    def write_to_file(path, data):
        with open(path, mode='w', encoding="utf-8_sig") as file:
            file.write(data)


## eel用
def read_from_csv():
    item_master = []
    with open("./source.csv") as f:
        for code, item, price in csv.reader(f):
            item_master.append(Item(code, item, price))
    return item_master

def hasItem(item_code):
    item_list = read_from_csv()
    for item in item_list:
        if (item_code == item.item_code) {
            return True
        }
    return False
        
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))

    # オーダーを登録
    order = Order(item_master)
    return order

if __name__ == "__main__":
    main()
