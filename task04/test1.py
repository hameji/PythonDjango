import csv

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print(f"商品コード: { item }")

    def get_order_list(self):
        for item_code in self.item_order_list:
            for order in self.item_master:
                if order.item_code == item_code:
                    print(f"商品名: {order.item_name}, {order.price}")

        
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))

    # ファイルから商品登録
    item_list = []
    with open("./source.csv") as f:
        for code, item, price in csv.reader(f):
            print(f"【追加】コード: {code}, 商品: {item}, 値段:{price}")
            item_master.append(Item(code, item, price))

    # オーダーを登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")

    # オーダー追加プロンプト
    order_no = input("オーダー商品番号を入力ください")
    item_list = []
    for order_item in order.item_master:
        item_list.append(order_item.item_code)
    # 該当コードの商品があるか判別、ある場合にオーダーに追加
    if order_no in item_list:
        print(order_no, "は存在するよ")
        order.add_item_order(order_no)
    else:
        print("その商品コードで登録されているアイテムはありません。")

    # 全商品の表示
    print("【全リスト】")
    for order_item in order.item_master:
        print(order_item.item_code, order_item.item_name, order_item.price)

    # オーダー表示
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    print("【オーダーコード】")
    order.view_item_list()
    # オーダー内容表示
    print("【オーダー商品】")
    order.get_order_list()
    
if __name__ == "__main__":
    main()
