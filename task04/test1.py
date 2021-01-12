import csv

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
        
    def view_item_list(self):
        for request in self.item_order_list:
            print(f"商品コード: { request.item_code }, 数量: { request.item_amount }")

    def get_order_list(self, money):
        total_price = 0
        for request in self.item_order_list:
            item_code = request.item_code
            for item in self.item_master:
                if item.item_code == item_code:
                    print(f"商品コード: {item.item_code}, 商品名: {item.item_name}, 金額: {item.price}, 数量: {request.item_amount}")
                    total_price += item.price * int(request.item_amount)
        print(f"合計金額は {total_price} 円 です。")    
        print(f"お預り金は{money} 円です。")
        if total_price < money:
            change = money - total_price
            print(f"お預り金は{money}なので、お釣りは{change}円となります。")
        else:
            shortage = total_price - money
            print(f"{shortage} 円不足しています。")
        
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))

    ## 課題3
    # # ファイルから商品登録
    # item_list = []
    # with open("./source.csv") as f:
    #     for code, item, price in csv.reader(f):
    #         print(f"【追加】コード: {code}, 商品: {item}, 値段:{price}")
    #         item_master.append(Item(code, item, price))

    # オーダーを登録
    order=Order(item_master)
    order.add_item_order(Request("001", 5))
    order.add_item_order(Request("002",3))
    order.add_item_order(Request("003",1))

    ## 課題6
    input_money = input("お預かり金額を入力してください")
    if input_money.isdecimal():
        print("正しい値が入力されました")
    else:
        print("入力値が正しくありません。")
        return

    ## 課題2, 課題4
    # # オーダー追加プロンプト
    # order_no = input("オーダー商品番号を入力ください")
    # order_amount = input("オーダー個数を入力してください")
    # item_list = []
    # for order_item in order.item_master:
    #     item_list.append(order_item.item_code)
    # # 該当コードの商品があるか判別、ある場合にオーダーに追加
    # if order_no in item_list:
    #     print(order_no, "は存在するよ")
    #     order.add_item_order(Request(order_no, order_amount))
    # else:
    #     print("その商品コードで登録されているアイテムはありません。")

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
    order.get_order_list(int(input_money))
    
if __name__ == "__main__":
    main()
