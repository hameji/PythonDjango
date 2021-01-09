from logging import exception
import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import datetime as dt
import pandas as pd

if os.name == "nt": #Windows
    new_line_code = "\r\n"
elif os.name == "posix": #Mac
    new_line_code = "\n"

# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)


def get_time():
    now = dt.datetime.now().strftime("%Y%m%d")
    return now

def take_log(event):
    now = get_time()
    log = f"{now}, {event} {new_line_code}"
    with open("log.txt", mode="a", encoding="utf-8_sig") as f:
        f.writelines(log)


# main
def main():
    take_log("起動した")
    search_keyword = "高収入"
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    
    driver.get("https://tenshoku.mynavi.jp/")
    take_log("ページの読み込み成功")
    time.sleep(5)
 
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(5)
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
    except:
        pass

    
    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()
    take_log("キーワード送信成功")


    ## 課題5に tryを追加, 
    ## 変数を用い、どの要素が問題かわかるようにしてみた。

    take_log("スクレイピング開始")
    job_info = driver.find_elements_by_class_name("cassetteRecruit")
    job_data = []
    colum_name = []
    for info in job_info:
        job_datum = []
        try:
            name = info.find_element_by_class_name("cassetteRecruit__name").text
            content_list = info.find_element_by_class_name("cassetteRecruit__main")
            tr_list = content_list.find_elements_by_tag_name("tr")
            job_datum.append(name)

            colum_name.clear
            for tr in tr_list:
                item = tr.find_element_by_tag_name("th").text
                value = tr.find_element_by_tag_name("td").text
                print("item:", item, "value:", value)
                job_datum.append(value)
                colum_name.append(item) ## <-何度も回って少し無駄な気しますが、わざわざそれだけ取り出すコード書くのも面倒なので、、、

            job_data.append(job_datum)
            colum_name.insert(0, "会社名")
        except exception as e:
            take_log("error while getting " + e)
            pass
        else:
            take_log(f"succeeded scraping {name}")
            pass
        finally:
            print(job_data)


    df = pd.DataFrame(job_data)
    if len(df.columns) == len(colum_name):
        df.columns = colum_name

    print(df)

    df.to_csv("data.csv")
        


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
